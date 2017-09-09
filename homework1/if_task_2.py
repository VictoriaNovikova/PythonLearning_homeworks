def compare(first, second):
    if first == second:
        return 1
    elif second == "learn":
        return 3
    elif len(first) > len(second):
        return 2