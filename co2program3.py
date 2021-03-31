Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> NumList = []
>>> Number = int(input("Please enter the Total Number of List Elements : "))
Please enter the Total Number of List Elements : 4
>>> for i in range(1, Number + 1):
	value = int(input("Please enter the Value of %d Element : " %i))
	NumList.append(value)

	
Please enter the Value of 1 Element : 1
Please enter the Value of 2 Element : 2
Please enter the Value of 3 Element : 3
Please enter the Value of 4 Element : 4
>>> total = sum(NumList)
>>> print("\n The Sum of All Element in this List is : ", total)

 The Sum of All Element in this List is :  10
>>> 