#!/usr/bin/env python3
"""
Scheduler for Daily Git Commits
Runs the daily commit script at specified time every day.
"""

import schedule
import time
import subprocess
import sys
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('daily_commit_scheduler.log'),
        logging.StreamHandler()
    ]
)

class DailyCommitScheduler:
    def __init__(self, repo_path, commit_script_path=None, schedule_time="09:00"):
        self.repo_path = Path(repo_path)
        self.schedule_time = schedule_time
        
        # Default to the daily commit script in the same directory
        if commit_script_path:
            self.commit_script = Path(commit_script_path)
        else:
            self.commit_script = Path(__file__).parent / "daily_git_commit.py"
    
    def run_daily_commit(self):
        """Execute the daily commit script"""
        try:
            logging.info("Starting daily commit process...")
            
            # Run the daily commit script
            result = subprocess.run([
                sys.executable, 
                str(self.commit_script), 
                str(self.repo_path)
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info("Daily commit completed successfully")
                logging.info(f"Output: {result.stdout}")
            else:
                logging.error(f"Daily commit failed with return code {result.returncode}")
                logging.error(f"Error: {result.stderr}")
                
        except Exception as e:
            logging.error(f"Exception during daily commit: {str(e)}")
    
    def start_scheduler(self):
        """Start the daily scheduler"""
        logging.info(f"Starting daily commit scheduler for {self.repo_path}")
        logging.info(f"Scheduled time: {self.schedule_time}")
        logging.info(f"Commit script: {self.commit_script}")
        
        # Schedule the daily commit
        schedule.every().day.at(self.schedule_time).do(self.run_daily_commit)
        
        # Also run immediately for testing (optional)
        logging.info("Running initial commit...")
        self.run_daily_commit()
        
        # Keep the scheduler running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Schedule daily git commits')
    parser.add_argument('repo_path', help='Path to your git repository')
    parser.add_argument('--time', default='09:00', help='Time to run daily commit (HH:MM format)')
    parser.add_argument('--script', help='Path to daily commit script')
    
    args = parser.parse_args()
    
    scheduler = DailyCommitScheduler(
        repo_path=args.repo_path,
        commit_script_path=args.script,
        schedule_time=args.time
    )
    
    try:
        scheduler.start_scheduler()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user")

if __name__ == "__main__":
    main()