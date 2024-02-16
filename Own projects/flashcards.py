from tkinter import *
from random import randint

root = Tk()
root.title('Chinese Language Flashcards')
root.geometry("420x500")



word = [(("Ich"),("我")),
		(("Du"),("你")),
		(("Sie"),("她")),
		(("Er"),("他")),
		(("Wir"),("我们")),
		(("Ihr"),("你闷"))
		]

# get count of word list
count = len(word)

def next():
	# Clear the screen
	answer_label.config(text="")
	my_entry.delete(0, END)

	# Create random selection
	global random_word
	random_word = randint(0, count-1)
	# update label with Chinese word
	chinese_word.config(text=word[random_word][1])

def answer():
	if my_entry.get().capitalize() == word[random_word][0]:
		answer_label.config(text=f"Correct! {word[random_word][1]} is {word[random_word][0]}")
	else:
		answer_label.config(text=f"Incorrect! {word[random_word][1]} is not {word[random_word][0]}")



chinese_word = Label(root, text="", font=("Helvetica", 36))
chinese_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("",18))
my_entry.pack(pady=20)


# Create Buttons 
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1, padx=20)


# Run next function when program starts
next()

root.mainloop()