import sys
from datetime import date

def calculate_ages_from_birthdates():
	if len(sys.argv) <2:
		print("Error: Write input file name")
		print("Example: python 03_3_birthdate.py names.csv")
		return

	input_file = sys.argv[1]
	today = date.today()

	try:
		with open(input_file, 'r') as infile:
			for line in infile:
				line = line.strip()
				if not line or ',' not in line:
					continue
				name, birthdate_string = line.split(',')
				name = name.strip()
				try:
					birthdate = date.fromisoformat(birthdate_string.strip())
					age = today.year - birthdate.year
					if (today.month, today.day) < (birthdate.month, birthdate.day):
						age -=1
					print(f"{name}, {age}")
				except (ValueError,UnboundLocalError):
					print(f"Failed to parse date for {name}: {birthdate_string}")
	except FileNotFoundError:
		print(f"Error: File '{input_file}' not found")
if __name__ == "__main__":
	calculate_ages_from_birthdates()
