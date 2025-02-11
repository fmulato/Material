"""
Counts the occurrences of different loop types in a Python file.
"""

def count_loops(filename: str) -> dict:
    """
    Reads a file and counts the occurrences of 'for', 'while', and 'if' loops.

    Args:
        filename: The path to the file.

    Returns:
        A dictionary containing the counts of each loop type.
    """

    loop_counts = {"for": 0, "while": 0, "if": 0}
    try: # Open the file and read it line by line
        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.strip() # Remove leading/trailing whitespace
                for loop_type in loop_counts: # Check if line contains a loop type
                    if line.startswith(loop_type): # Increment the count for that loop type
                        loop_counts[loop_type] += 1
                        break  # Avoid counting a line as multiple loop types
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.") #
        return None

    return loop_counts


def main():
    """
    Main function to get user input and display loop counts.
    """

    filename = input("Enter program filename: ")
    loop_counts = count_loops(filename) # call function to count loops

    if loop_counts:
        for loop_type, count in loop_counts.items():
            print(f"Program {filename} contains {count} {loop_type} loops")


if __name__ == '__main__':
    main()
