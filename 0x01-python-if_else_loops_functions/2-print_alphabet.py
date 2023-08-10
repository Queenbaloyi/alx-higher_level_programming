#!/usr/bin/python3
def get_alphabet_letters():
    """Returns a list of all the lowercase letters."""
    alphabet_letters = []
    for letter in range(97, 123):
        alphabet_letters.append(chr(letter))
    return alphabet_letters

def print_alphabet():
    """Prints the lowercase letters of the alphabet, not followed by a new line."""
    alphabet_letters = get_alphabet_letters()
    for letter in alphabet_letters:
        print(letter, end="")

if __name__ == "__main__":
    print_alphabet()
