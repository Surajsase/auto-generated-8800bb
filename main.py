import json

def calculate_sum(upstream_data):
    """Calculate the sum of numbers in the upstream data."""
    numbers = upstream_data.get('numbers', [])
    return sum(numbers)

def calculate_average(upstream_data):
    """Calculate the average of numbers in the upstream data."""
    numbers = upstream_data.get('numbers', [])
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main(upstream_results):
    """Main function that calls the logic functions and prints results to stdout."""
    upstream_data = json.loads(upstream_results)
    sum_result = calculate_sum(upstream_data)
    average_result = calculate_average(upstream_data)
    print(f"Sum: {sum_result}")
    print(f"Average: {average_result}")

if __name__ == "__main__":
    main('{"numbers": [1, 2, 3, 4, 5]}')