# Author: Erik Rumppe
# Date: 7/22/2026

def read_scores(filename):
    scores = []
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            scores.append((name, int(score)))
    return scores

def calculate_average(scores):
    total = sum(score for _, score in scores)
    return total / len(scores)

def write_report(scores, average):
    with open('report.txt', 'w') as file:
        file.write("Test Results\n")
        file.write("=============================\n\n")
        for name, score in scores:
            file.write(f"{name}: {score}\n")
        file.write(f"\nClass Average: {average:.2f}")

# Main process
scores = read_scores('scores.txt')
# Test the function
###### Prints encoding errors to the terminal but not the files.  Interesting.....
#print(read_scores('scores.txt'))

average = calculate_average(scores)
# Test the function
#print(f"Average score: {calculate_average(scores):.2f}")

write_report(scores, average)
print("Report generated in 'report.txt'!")