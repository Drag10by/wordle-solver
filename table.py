def tablo(words):

	row = 6	
	column,b = divmod(len(words),row)

	x = 6

	

	print("\n       |",end="")

	

	for i in range(x):

		print(f"   {i}   |",end="")

		

	print()

	

	for i in range(column+1):	

		m = ""

		print("'"*7,"|",sep="",end="")

		if i == column:

			row = b

		for j in range(row):

			print("'"*7,"|",sep="",end="")

			k = words[i*x+j]

			m+= f" {k} |"

		print()

		h = ' '*(7-len(str(i)))

		print(f"{i}{h}|{m}")

		for g in range(row+1):

			print("_"*7,"|",sep="",end="")

		print()
