# can use single qoutes/ double
Name = "Michael Jackson"
print(Name[0:5])

# can use negative indexing
print(Name[-5:-1])

# can skip
print(Name[::2])

# Slicing every second value inside index 5
print(Name[0:5:2])

# String manipulation
a = 'Thriller is the sixth studio album'
print("before upper: ", a)
print("after upper:", a.upper())

# reg ex: tool for matching and handling strings
import re
s1 = "The BodyGaurd is the best album"
pattern = r"Body"
result = re.search(pattern, s1)
if result:
    print("Match found!")
else:
    print("Match not found")