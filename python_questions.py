#
import pandas as pd
import numpy as np

# Reverse of string
str1 = 'Aravind'
rever_str = str1[::-1]
rever_str

# Palindrome or not
def palindrome(input_val):
    rever_str = input_val[::-1].lower()
    if rever_str==input_val.lower():
        print("Palindrome")
    else:
        print("Not Palindrome")
    return None

# PRime
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        print(i)
        if n%i == 0:
            return False
    return True
