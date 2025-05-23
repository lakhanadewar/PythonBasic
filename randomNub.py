import random
import matplotlib.pyplot as plt

# Initialize a dictionary to store counts of each number
number_counts = {i: 0 for i in range(1, 101)}

# Generate numbers 1000 times
for _ in range(100):
    num = random.randint(1, 10)
    number_counts[num] += 1

# Calculate percentages
total_generations = 100
number_percentages = {num: (count / total_generations) * 100 for num, count in number_counts.items()}

# Prepare data for plotting
numbers = list(number_percentages.keys())
percentages = list(number_percentages.values())

# Create the plot
plt.figure(figsize=(15, 6))
plt.bar(numbers, percentages)
plt.title(f'Percentage Distribution of Random Numbers (1-10) over {total_generations} Generations')
plt.xlabel('Number')
plt.ylabel('Percentage (%)')
plt.xticks(range(1, 11), rotation=9)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()
plt.show()

# Print some statistics
print(f"Total generations: {total_generations}")
print(f"Minimum percentage: {min(percentages):.2f}% (Number {numbers[percentages.index(min(percentages))]})")
print(f"Maximum percentage: {max(percentages):.2f}% (Number {numbers[percentages.index(max(percentages))]})")
print(f"Average percentage: {sum(percentages)/len(percentages):.2f}%")