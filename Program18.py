Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first_Dict = {1: 'apple', 2: 'Banana' , 3: 'Orange'}
>>> second_Dict = { 4: 'Grape', 5: 'Mango'}
>>> print("First Dictionary: ", first_Dict)
First Dictionary:  {1: 'apple', 2: 'Banana', 3: 'Orange'}
>>> print("Second Dictionary: ", second_Dict)
Second Dictionary:  {4: 'Grape', 5: 'Mango'}
>>> first_Dict.update(second_Dict)
>>> print("\nAfter Merging two Dictionaries : ")

After Merging two Dictionaries : 
>>> print(first_Dict)
{1: 'apple', 2: 'Banana', 3: 'Orange', 4: 'Grape', 5: 'Mango'}
>>> 