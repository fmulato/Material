"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""

def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename = input("Enter program filename: ")
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        num_for_loops = 0

    for line in lines:
        if line.strip().startswith("for"):
            num_for_loops += 1

    print(f"Program {filename} contain {num_for_loops} for loops")


    num_while_loops = 0
    for line in lines:
        if line.strip().startswith("while"):
            num_while_loops += 1

    print(f"Program {filename} contain {num_while_loops} while loops")

    num_if_loops = 0
    for line in lines:
        if line.strip().startswith("if"):
            num_if_loops += 1

    print(f"Program {filename} contain {num_if_loops} if loops")

if __name__ == '__main__':
    main()
