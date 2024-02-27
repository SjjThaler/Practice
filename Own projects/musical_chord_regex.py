import re

def validate_chord(chord):
    # Regular expression pattern for validating chord notation
    pattern = r'^[A-G](#|b)?(m|maj|dim|aug|sus2|sus4)?(6|7|9|11|13)?(\(add\d+\))?$'
    
    # Using re.match to check if the chord matches the pattern
    if re.match(pattern, chord):
        print("The chord is valid.")
    else:
        print("The chord is invalid.")


validate_chord("Cmaj7")
validate_chord("Cmaj(add9)")

