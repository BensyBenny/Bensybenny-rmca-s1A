Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "I am programmer. I am student."
>>> word = "am"
>>> words = string.split()
>>> count = 0
>>> for w in words:
	if w == word:
		count += 1
		print(count)

		
1
2
>>> 