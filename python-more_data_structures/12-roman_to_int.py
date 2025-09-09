#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    total = 0
    rom_val = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    i = 0
    while i < len(roman_string):
        if roman_string[i] not in rom_val:
            i += 1
            continue

        current = rom_val[roman_string[i]]
        if i < len(roman_string) - 1:
            next = rom_val[roman_string[i + 1]]
            if next > current:
                total += next - current
                i += 1
            else:
                total += current
        else:
            total += current
        i += 1

    return total


def is_power_of_10(value):
    return str(value)[0] == "1"
