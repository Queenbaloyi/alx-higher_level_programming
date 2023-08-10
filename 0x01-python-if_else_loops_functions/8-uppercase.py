def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print(c, end="")
    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
