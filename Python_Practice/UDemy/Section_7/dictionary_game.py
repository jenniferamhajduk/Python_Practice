locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = { 0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = { "quit": "Q",
          "west": "W",
          "east": "E",
          "south": "S",
          "north": "N",
          "road": "1",
          "hill": "2",
          "building": "3",
          "valley": "4",
          "forest": "5"}

named_exits = { 1: {"2": 2, "3": 3, "5": 5, "4": 4},
                2: {"5": 5},
                3: {"1": 1},
                4: {"1": 1, "2": 2},
                5: {"2": 2, "1": 1}}


loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(named_exits[loc])

    direction = input("Avalable exits are: " + availableExits.upper() + " ")
    print()
    if len(direction) > 1:
        # for word in vocabulary:
        #     if word in direction.lower():
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word.lower() in vocabulary:
                direction = vocabulary[word.lower()]
                break
    
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction!")



