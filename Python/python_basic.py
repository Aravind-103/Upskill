import pandas as pd
import numpy as np
import plotly.express as px

print("Hello World!:)")
print("Hi, I'm Aravind")
print("I am learning Python and Data Science")
print("Welcome to the world of Data Science and Machine Learning")

# Reverse a string
text = "Python"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


# Count repeated characters in a string
string = "AravindGaddam"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1
print("Character count:", char_count)
print("Character appears often", max(char_count, key=char_count.get))

# String flattening
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)
# Output: [1, 2, 3, 4, 5, 6]

