import sys
def update_ages_flexible():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	try:
		years_to_add = int(sys.argv[3])
	except IndexError:
		years_to_add = 5
	with open(input_file, 'r') as infile, open (output_file, 'w') as outfile:
		for line in infile:
			line = line.strip()
			if not line or ',' not in line:
				outfile.write(line + '\n')
				continue
			name, age_str = line.split(',')
			name = name.strip()
			age_str = age_str.strip()
			try:
				age = int(age_str)
				new_age = age + years_to_add
				outfile.write(f"{name},{new_age}\n")
			except ValueError:
				outfile.write(f"{name},{age_str}\n")
update_ages_flexible()
