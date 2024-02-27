import re

def validate_chord(chord):
    # Regular expression pattern for validating Roman numeral chord notation
    pattern = r'^[A-G](#|b)?(m|maj|dim|aug|sus2|sus4)?(7|7b5)?(#|b)?(6|9|11|13)?(\(add\d+\))?$'
    
    # Using re.match to check if the chord matches the pattern
    if re.match(pattern, chord):
        print("The chord is valid.")
    else:
        print("The chord is invalid.")


# Testing major seventh chord
validate_chord("Cmaj7")

# Testing major ninth chord
validate_chord("Cmaj(add9)")
validate_chord("Cmaj9")

# Testing dominant 7th chord
validate_chord("G7")

# Testing minor seventh flat five chord
validate_chord("Am7b5")

# Testing raised ninth
validate_chord("Emaj#9")

# Testing seventh chord with raised 11th
validate_chord("Fmaj7#11")

