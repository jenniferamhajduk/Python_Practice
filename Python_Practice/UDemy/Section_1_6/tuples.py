# # # t = ("a", "b", "c")
# # # name = "Jennifer"
# # # print(t, name)
# # # print((t, name))

# # metallica = "Run of the lightning", "EP", 1984
# # # metallica2 = list(metallica)
# # # print(metallica2)

# # # data = 1,2,26
# # # x,y,z = data
# # # print(x)
# # # print(y)
# # # print(z)

# # title, artist, year = metallica
# # print(title)
# # print(artist)
# # print(year)

# # table = ("coffee table", 200, 100, 75, 34.50)
# # print(table[1] * table[2])

# # name, length, width, height, price = table
# # print(length * width)

# # #nested tuples

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981)
         ]

# print(len(albums))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))



