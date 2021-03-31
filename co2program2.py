Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> n = int(input("Enter the value of 'n': "))
Enter the value of 'n': 8
>>> a = 0
>>> b = 1
>>> sum = 0
>>> count = 1
>>> print("Fibonacci Series: ", end = " ")
Fibonacci Series:  
>>> while(count <= n):
      print(sum, end = " ")
      count += 1
      a = b
      b = sum
      sum = a + b

      
0 1 1 2 3 5 8 13 
>>> 