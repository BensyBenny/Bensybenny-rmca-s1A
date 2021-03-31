Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> vowels = ['a', 'e', 'i', 'o', 'i', 'u']
>>> count = vowels.count('i')
print('The count of i is:', count)
>>> count = vowels.count('p')
print('The count of p is:', count)
>>> random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
>>> count = random.count(('a', 'b'))
>>> print("The count of ('a', 'b') is:", count)
The count of ('a', 'b') is: 2
>>> count = random.count([3, 4])
>>> print("The count of [3, 4] is:", count)
The count of [3, 4] is: 1
>>> 