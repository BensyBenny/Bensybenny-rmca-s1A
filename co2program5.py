Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rows = 5
>>> for i in range(0, rows):
	for j in range(i + 1):
		print(i * j, end='  ')
	print()

	
0  
0  1  
0  2  4  
0  3  6  9  
0  4  8  12  16  
>>> 