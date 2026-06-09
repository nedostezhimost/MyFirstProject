#!/usr/bin/env python3
import json
name = input("What is your name? ")
print(f"Hello {name}!")
while True:
	gender = input("What is your gender (B/G)?").upper().strip()
	if gender in ['B', 'G']:
	   break
	print("please enter 'b' for boy or 'g' for girl.")
while True:
	try:
		age_input = input("How old are you? ").replace('"', "").strip()
		age = int(age_input)
		if age < 0 or age >120:
			print("Please, enter a realistic age!")
			continue
		print(f"Oh, {age} is very young!")
		break
	except ValueError:
		print("Please enter a valid number")
if age < 12:
	print(f"You are a child!")
	activity_place = input("What primary school do you go to?")
	likes_it = input("Do you like it there (yes/no)?")
elif 12<= age <= 18:
	print(f"You are a teenager!")
	activity_place = input("What college or school do you go to?")
	likes_it = input("Do you like it there?")
else:
	print (f"You are an adult!")
	activity_place = input("Where do you work?")
	likes_it = input("Do you like it there (yes/no)?")
print(f"In 20 years you will be working hard! You will be {age + 20}")
print(f"In 70 years  you might be retired. You will be {age + 70}")
if 5<= age <= 11:
	print(f"You go to the primary school.")
elif 12<= age <= 16:
	print(f"You go to secondary school.")
	print(f"I know {activity_place}, this is the great place to study!")
if 19<= age <=64:
	choice = input(f"Do you go to an university or job?")
	if choice == "university":
		university = input("What university do you go at?")
		input(f"It's a great university! Do you like it?")
		print(f"Nice.")
	elif choice == "job":
		job = input(f"What is your proffesion?")
		input(f"Do you like your job?")
user_data = {
	"name": name,
	"age": age,
	"gender": gender,
	"place": activity_place,
	"likes it": likes_it
}
file_name = f"{name.lower().replace(' ', '_')}_info.json"
with open(file_name, 'w') as file:
	json.dump(user_data, file, indent =4)
print(f"\nAll data saved succesfully!")
