# Task 4: Implement a program to check if a string is a palindrome, ignoring spaces and case sensitivity.
def is_palindrome(input_string):
  # Preprocess the string: remove spaces and convert to lowercase
  cleaned_string = input_string.replace(" ", "").lower()
  return cleaned_string == cleaned_string[::-1]

test_strings =[
 "A man a plan a canal panama",
 "racecar",
 "hello",
 "was it a car or a cat i saw?",
 "no lemon no melon"
]

for s in test_strings:
  if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
  else:
    print(f'"{s}" is not a palindrome.')