def check_ages_robust(filename):
	with open(filename, 'r') as file:
		for line in file:
			line = line.strip()
			if ',' not in line:
				continue
			name, age_str = line.split(',')
			name = name.strip()
			age_str = age_str.strip()
			try:
				age = int(age_str)
				if age >=16:
					print(name)

			except ValueError:
				print("Failed to parse age from this row of csv!!")
				continue
check_ages_robust('users.csv')
print("--- end ---")
