"""
Filter names from list that starts with "a" or "A" using lambda function
•	 ["Alex", "Bob", "dan", "ash"] => ["Alex", "ash"]
"""


def filter_name_starting_with_a(names: list[str]) -> list[str]:
    return list(filter(lambda name: name[0].upper().startswith('A'), names))


if __name__ == "__main__":
    print(filter_name_starting_with_a(["Alex", "Bob", "dan", "ash"]))
