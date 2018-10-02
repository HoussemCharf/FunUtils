import string, random

def generate():
	letters = string.ascii_lowercase + string.digits + string.ascii_uppercase 
	try:
		length = int(input("Enter name length: "))
		print(''.join(random.choice(letters) for i in range(length)))
	except ValueError:
		print("Please enter a number.")
		generate()

generate()
