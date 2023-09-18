#Problem 2 :Determine whether a given string is Palindrome
str = input ("Enter a string: ")
rev_str = reversed (str)
if list (str) == list (rev_str):
   print ("True : Palindrome")
else:
   print ("False : Not palindrome")
