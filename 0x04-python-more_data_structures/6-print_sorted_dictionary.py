def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    Args:
        a_dictionary: A dictionary.

    Returns:
        None.
    """

    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
