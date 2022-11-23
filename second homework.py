from string import ascii_lowercase as alpha
def alphabet_position(word):
    return ' '.join(str(alpha.index(letter) + 1) for letter in word.lower() if letter in alpha)