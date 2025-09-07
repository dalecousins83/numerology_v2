# Core numerology math functions

LETTER_MAP = {
    "A": 1, "J": 1, "S": 1,
    "B": 2, "K": 2, "T": 2,
    "C": 3, "L": 3, "U": 3,
    "D": 4, "M": 4, "V": 4,
    "E": 5, "N": 5, "W": 5,
    "F": 6, "O": 6, "X": 6,
    "G": 7, "P": 7, "Y": 7,
    "H": 8, "Q": 8, "Z": 8,
    "I": 9, "R": 9
}

def reduce_number(num: int) -> int:
    """Reduce to core digit, allow Master Numbers 11, 22."""
    while num > 9 and num not in (11, 22):
        num = sum(int(d) for d in str(num))
    return num

def name_to_number(name: str, vowels_only=False, consonants_only=False) -> int:
    """Convert name to number, optionally filter vowels/consonants."""
    vowels = "AEIOU"
    total = 0
    for char in name.upper():
        if char not in LETTER_MAP:
            continue
        if vowels_only and char not in vowels:
            continue
        if consonants_only and char in vowels:
            continue
        total += LETTER_MAP[char]
    return reduce_number(total)

def date_to_number(day: int, month: int, year: int) -> int:
    """Convert DOB into Life Path number."""
    return reduce_number(sum(int(d) for d in f"{day}{month}{year}"))
