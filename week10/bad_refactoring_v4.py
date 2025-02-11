"""
Refactored version of the code in bad_refactoring_v3.py
>>> count_loops('bad_refactoring.py')
{'for': 3, 'while': 0, 'if': 3}
"""

def read_file(filename: str) -> list[str] | None:
    """Reads a file and returns its lines as a list of strings.

    Args:
        filename: The path to the file.

    Returns:
        A list of strings, where each string is a line from the file, or None if
        the file is not found.
    """
    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def process_loops(lines: list[str]) -> dict:
    """Counts the occurrences of different loop types in a list of lines.

    Args:
        lines: A list of strings, where each string represents a line of code.

    Returns:
        A dictionary containing the counts of each loop type.
    """
    loop_counts = {"for": 0, "while": 0, "if": 0}
    for line in lines:
        line = line.strip()
        for loop_type in loop_counts:
            if line.startswith(loop_type):
                loop_counts[loop_type] += 1
                break  # Count a line only for one loop type
    return loop_counts


def count_loops(filename: str) -> dict | None:
    """
    Reads a file and counts the occurrences of 'for', 'while', and 'if' loops.

    Args:
        filename: The path to the file.

    Returns:
        A dictionary containing the counts of each loop type, or None if the file is not found.
    """
    lines = read_file(filename)
    if lines is None:
        return None  # Propagate file not found error

    return process_loops(lines)


if __name__ == '__main__':
    filename = input("Enter program filename: ")
    loop_counts = count_loops(filename)

    if loop_counts:
        for loop_type, count in loop_counts.items():
            print(f"Program {filename} contains {count} {loop_type} loops")
