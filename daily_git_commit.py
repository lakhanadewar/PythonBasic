#!/usr/bin/env python3
"""
Daily Git Commit Automation Script
Automatically adds content to your project and commits changes daily.
"""

import os
import subprocess
import datetime
import json
import random
from pathlib import Path

class DailyGitCommitter:
    def __init__(self, repo_path, config_file="commit_config.json"):
        self.repo_path = Path(repo_path)
        self.config_file = self.repo_path / config_file
        self.load_config()
    
    def load_config(self):
        """Load configuration or create default config"""
        default_config = {
            "commit_messages": [
                "Daily update - {date}",
                "Automated daily commit - {date}",
                "Daily progress - {date}",
                "Regular update - {date}"
            ],
            "file_to_update": "daily_log.md",
            "content_type": "log",  # Options: log, todo, notes, code_comment
            "branch": "main"
        }
        
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """Save current configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def run_git_command(self, command):
        """Execute git command and return result"""
        try:
            result = subprocess.run(
                command, 
                cwd=self.repo_path, 
                capture_output=True, 
                text=True, 
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {' '.join(command)}")
            print(f"Error: {e.stderr}")
            return None
    
    def check_git_status(self):
        """Check if there are changes to commit"""
        status = self.run_git_command(['git', 'status', '--porcelain'])
        return bool(status)
    
    def add_daily_content(self):
        """Add daily content based on configuration"""
        today = datetime.date.today()
        file_path = self.repo_path / self.config["file_to_update"]
        
        content_generators = {
            "log": self.generate_log_content,
            "todo": self.generate_todo_content,
            "notes": self.generate_notes_content,
            "code_comment": self.generate_code_comment
        }
        
        content_type = self.config.get("content_type", "log")
        generator = content_generators.get(content_type, self.generate_log_content)
        
        new_content = generator(today)
        
        # Append content to file
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added daily content to {file_path}")
    
    def generate_log_content(self, date):
        """Generate daily log content"""
        activities = [
            "Code review and optimization",
            "Documentation updates",
            "Bug fixes and improvements",
            "Feature development progress",
            "Testing and validation",
            "Refactoring and cleanup"
        ]
        
        activity = random.choice(activities)
        return f"""
## {date.strftime('%Y-%m-%d')} - Daily Update

- **Date**: {date.strftime('%A, %B %d, %Y')}
- **Activity**: {activity}
- **Status**: Completed daily development tasks
- **Notes**: Automated daily commit

---
"""
    
    def generate_todo_content(self, date):
        """Generate todo list content"""
        todos = [
            "Review pending pull requests",
            "Update project documentation",
            "Optimize database queries",
            "Write unit tests for new features",
            "Check for security vulnerabilities",
            "Update dependencies"
        ]
        
        selected_todos = random.sample(todos, 3)
        todo_list = '\n'.join([f"- [ ] {todo}" for todo in selected_todos])
        
        return f"""
# TODO - {date.strftime('%Y-%m-%d')}

{todo_list}

*Generated on {date.strftime('%A, %B %d, %Y')}*

---
"""
    
    def generate_notes_content(self, date):
        """Generate notes content"""
        return f"""
# Daily Notes - {date.strftime('%Y-%m-%d')}

**Date**: {date.strftime('%A, %B %d, %Y')}

## Development Notes
- Continued work on current sprint objectives
- Maintained code quality standards
- Regular project maintenance completed

## Next Steps
- Continue feature development
- Monitor system performance
- Plan upcoming releases

---
"""
    
    def generate_code_comment(self, date):
        """Add comment to a Python file"""
        comment_file = self.repo_path / "daily_comments.py"
        
        return f"""
# Daily update - {date.strftime('%Y-%m-%d')}
# Automated commit on {date.strftime('%A, %B %d, %Y')}
# Project maintenance and continuous development

"""
    
    def commit_and_push(self):
        """Commit changes and push to remote"""
        today = datetime.date.today()
        
        # Add all changes
        if not self.run_git_command(['git', 'add', '.']):
            return False
        
        # Create commit message
        commit_template = random.choice(self.config["commit_messages"])
        commit_message = commit_template.format(date=today.strftime('%Y-%m-%d'))
        
        # Commit changes
        if not self.run_git_command(['git', 'commit', '-m', commit_message]):
            return False
        
        # Push to remote
        branch = self.config.get("branch", "main")
        if not self.run_git_command(['git', 'push', 'origin', branch]):
            print("Warning: Push failed. You may need to configure remote or authentication.")
            return False
        
        print(f"Successfully committed and pushed: {commit_message}")
        return True
    
    def run_daily_commit(self):
        """Main method to run daily commit process"""
        print(f"Starting daily commit process at {datetime.datetime.now()}")
        print(f"Repository: {self.repo_path}")
        
        # Change to repository directory
        os.chdir(self.repo_path)
        
        # Add daily content
        self.add_daily_content()
        
        # Check if there are changes
        if not self.check_git_status():
            print("No changes to commit")
            return False
        
        # Commit and push
        return self.commit_and_push()

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Automate daily git commits')
    parser.add_argument('repo_path', help='Path to your git repository')
    parser.add_argument('--config', help='Custom config file path')
    parser.add_argument('--setup', action='store_true', help='Setup configuration')
    
    args = parser.parse_args()
    
    # Initialize committer
    config_file = args.config if args.config else "commit_config.json"
    committer = DailyGitCommitter(args.repo_path, config_file)
    
    if args.setup:
        setup_configuration(committer)
    else:
        committer.run_daily_commit()

def setup_configuration(committer):
    """Interactive setup for configuration"""
    print("=== Daily Git Commit Setup ===")
    
    # File to update
    current_file = committer.config.get("file_to_update", "daily_log.md")
    new_file = input(f"File to update daily [{current_file}]: ").strip()
    if new_file:
        committer.config["file_to_update"] = new_file
    
    # Content type
    content_types = ["log", "todo", "notes", "code_comment"]
    current_type = committer.config.get("content_type", "log")
    print(f"Content types: {', '.join(content_types)}")
    new_type = input(f"Content type [{current_type}]: ").strip()
    if new_type in content_types:
        committer.config["content_type"] = new_type
    
    # Branch
    current_branch = committer.config.get("branch", "main")
    new_branch = input(f"Git branch [{current_branch}]: ").strip()
    if new_branch:
        committer.config["branch"] = new_branch
    
    # Save configuration
    committer.save_config()
    print("Configuration saved!")

if __name__ == "__main__":
    main()