"""
=================================================
EVEN OR ODD CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a number
is Even or Odd.

-------------------------------------------------
Input Example:
7

Output Example:
Odd

=================================================
"""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
