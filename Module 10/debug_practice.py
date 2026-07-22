# Author: Erik Rumppe
# Date: 7/22/2026

def calculate_average(numbers):
    if not numbers:
        return 0   # Return 0 for empty list
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def main():
    data = [10, 5, 8, 12, 3, 7]
    average = calculate_average(data)
    maximum = find_max(data)
    print(f"The average is: {average}")
    print(f"The maximum is: {maximum}")

    empty_list = []
    empty_average = calculate_average(empty_list)
    empty_max = find_max(empty_list)
    print(f"Empty list average: {empty_average}")
    print(f"Empty list maximum: {empty_max}")

if __name__ == "__main__":
    main()
