#!/usr/bin/python3
def roman_to_int(roman_string):
    um = 0
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if type(roman_string) != str or roman_string == None:
        return 0
    if len(roman_string) == 0:
        return 0
    if len(roman_string) == 2:
        if rom[roman_string[1]] > rom[roman_string[0]]:
            return rom[roman_string[1]] - rom[roman_string[0]]
        else:
            return rom[roman_string[0]] + rom[roman_string[1]]
    for i in range(len(roman_string)):
        um += rom[roman_string[i]]
    return um
