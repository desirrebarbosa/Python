# range is an object that is an ordered list
for i in range(0,3):
    print(i)

dates = [1982, 1980, 1973, 2000]
year = dates[0]
i = 0
while(year != 1973):
    print(year)
    i = i + 1
    year = dates[i]

for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at: ", num)
        break
    print(num)

# did not execute print num because it went back up
# after contniue 
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

print("\n")
for i in range(-5, 6):
    print(i)

print("\n")
Genres = ["rock", "R&B", "Soundtrack", "Soul", "Pop"]
for i in range(len(Genres)):
    print(Genres[i])