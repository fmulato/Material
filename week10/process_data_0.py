"""
This script processes data in 3 steps: clean, transform, and summarize.
The clean_data function removes leading and trailing whitespaces from strings.
The transform_data function converts strings to uppercase.
The summarize_data function counts the frequency of each item in the data.

"""

def process_data(data):
    """
    Process data in 3 steps: clean, transform, and summarize.
    >>> process_data([1, '  hello  ', 3.14, 'world'])
    {1: 1, 'HELLO': 1, 3.14: 1, 'WORLD': 1}
    """

    # step 1: Clean data
    cleaned_data = []
    for item in data:
        if isinstance(item, str):
            item = item.strip()
        cleaned_data.append(item)

    # step 2: Transform data
    transformed_data = []
    for item in cleaned_data:
        if isinstance(item, str):
            item = item.upper()
        transformed_data.append(item)

    # step 3: Summarize data
    summary = {}
    for item in transformed_data:

        if item in summary:
            summary[item] += 1
        else:
            summary[item] = 1

    return summary


#if __name__ == '__main__':
    #data = [1, '  hello  ', 3.14, 'world', 'World ', 'hello']
    #result = process_data(data)
    #print(result)

