# are type of a collection, unordered
# behaves just like mathematical sets

set1 = {"pop", "rock", "soul", "hard rock"}
print(set1)

#can also convert list to set
# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set