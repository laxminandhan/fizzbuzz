"""Create a program that does text file copying"""

with open("20k.txt") as f:
	with open("20K_new.txt", "w") as f1:
		for line in f:
			f1.write(line)

