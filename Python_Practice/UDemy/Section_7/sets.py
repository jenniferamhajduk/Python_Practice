# #Sets do not contain duplicates and are unordered. union and intersection, immutable
# farm_animals = {"sheep", "cow", "hen"} #first set format, not key/value
# print(farm_animals)

# for animal in farm_animals:
#     print(animal)

# print("*" * 40)

# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"]) #pass list .to the set.
# print(wild_animals)

# for animal in wild_animals:
#     print(animal)

# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set() # must use the set constructor
# #union

# print(even)
# print(len(even))
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))

# print(even.intersection(squares))
# print(squares & even)
# print(sorted(squares))
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))

# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))


#symmetric difference - all in one or the other but not both
# print(sorted(even.symmetric_difference(squares))) #can go in either direction


# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# squares.remove(8) #remove raises an error, discard doesnt

#subsets - if all memebers are contained in another set
#supersets - contains all otehr sets members

even = set(range(0, 40, 2))
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")
 #frozen set - can be added as a member, can be used as a key in dictionary
even = frozenset(range(0, 100, 2))
print(even)


