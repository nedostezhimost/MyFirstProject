#!/usr/bin/env python3
name = input("What is your name? ")
print(f"Hello {name}!")
gender = input("What is your gender?")
try:
	age = int(input("How old are you? ").replace('"', ""))
	print(f"Oh, {age} is very young!")

except ValueError:
	print(f"Please enter a valid number next time!")
	exit()
if age < 12:
	print(f"You are a child!")
elif 12<= age <= 18:
	print(f"You are a teenager!")
else:
	print (f"You are an adult!")
print(f"In 20 years you will be working hard! You will be {age + 20}")
print(f"In 70 years  you might be retired. You will be {age + 70}")
if 5<= age <= 11:
	print(f"You go to the primary school.")
elif 12<= age <= 16:
	print(f"You go to secondary school.")
	school = input(f"What school do you go to, {name}?")
	print(f"I know {school}, this is the great school!")
if 16<= age <= 18:
	choice = input(f"Do you go to sixth form or college? (Type 'sixth form' or 'college'): ").lower().strip()
	if choice == "sixth form":
		school = input(f"what school did you study at before?")
		print(f"Oh, {school} sixth form is a great choice!")
	elif choice == "college":
		college = input(f"What college do you go to?")
		print(f"Wow, {college} sounds like a cool place to study")
	else:
		print(f"Ah, so you are doing something else! That's awesome.")
if 19<= age <=64:
	choice = input(f"Do you go to an university or job?")
	if choice == "university":
		university = input("What university do you go at?")
		answer = input("It's a great university! Do you like it?")
		if answer == "yes":
			print("Nice.")
		elif answer == "no":
			input("Why?")
	elif choice == "job":
		job = input("What is your proffesion?")
		input("Do you like your job?")
