
def search4vowels(word: str) -> set:

    """Return any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str) -> set:

    """Return any supplied in letter found in a supplied in phrase"""
    return set(letters).intersection(set(phrase))
