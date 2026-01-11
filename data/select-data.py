import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

print(df)

x = df[['ID']]
print(x)

# problem 1

dict = {'Student' : ['David', 'Samuel', 'Terry', 'Evan'],
        'Age' : [27, 24, 22, 32],
        'Country' : ['UK', 'Canada', 'China', 'USA'],
        'Course' : ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
        'Marks' : [85, 72, 89, 76]}

df2 = pd.DataFrame(dict)
print(df2)

b = df2[['Marks']]
print(b)

c = df2[['Country', 'Course']]
print(c)