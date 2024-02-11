# Returning first word of a text by determining the index of the first whitespace

def first_word(text):
    try:
        index = text.index(" ")
        return text[:index]
    # Return the input if there is no index because the string doesn't contain a whitespace
    except ValueError:
        return text