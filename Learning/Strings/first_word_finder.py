# My own attempt at finding the first word of a string

def first_word(text):
    count = 0
    for i in text:
        if i == " ":
            break
        else:
            count += 1

    return text[:count]

print(first_word("Greetings from Barcelona"))
print(first_word("Hello_World Hello"))
print(first_word("Hey!"))


# A better solution utilizing the find method

def better_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

print(better_word("Gree tings"))
print(better_word("Hey!"))


