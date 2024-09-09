# Task 2: Create a program that reverses a list without using builtin functions and prints both the original and reversed lists.
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

original_lst = [10,11,12,13,14,15]
print("Original List: ",original_lst)
print("Reverse List: ",Reverse(original_lst))