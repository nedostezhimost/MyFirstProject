import sys
import math
def get_total_area():
	if len(sys.argv) < 2:
		print("Error: write file name. Example: python 04_0_total_area.py shapes.csv")
		return

	filename = sys.argv[1]
	total_area = 0.0

	try:
		with open(filename, 'r') as file:
			for line in file:
				line = line.strip()
				if not line:
					continue
				parts = line.split(',')
				shape_type = parts[0].strip().upper()
				sides = [float(x.strip()) for x in parts[1:] if x.strip()]
				if shape_type == 'S':
					print(f"shape is square with sides {sides}")
					area = sides[0] * sides[1]
					total_area += area
				elif shape_type == 'T':
					print(f"shape is triangle with sides {sides}")

					a, b, c = sides[0], sides[1], sides[2]
					s = (a + b + c) / 2
					area = math.sqrt(s * (s - a) * (s - b) * (s - c))
					total_area += area
		print(f"Total area: {total_area:.2f} m²")
	except FileNotFoundError:
		print(f"Error: File '{filename}' not found")
	except Exception as e:
		print(f"Error processing file: {e}")
if __name__ == "__main__":
	get_total_area()
