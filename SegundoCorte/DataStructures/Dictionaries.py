#{Diccionaries: Key words, value}

#Example 1
print("Example 1")
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors)
print(num_cameras)
print()

#Example 2 
print("Example 2")
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
print()

#Example 3
print("Example 3")
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"] , 111 : 9} #admite todo tipo de datos, incluso listas
print(children)
print()

#Example 4
print("Example 4")
my_empty_ditionary = {}
print(my_empty_ditionary)

my_empty_ditionary ["dinosaurs"] = 0
print(my_empty_ditionary)
print()

#Example 5
print("Example 5")
animals_in_zoo = {"zebras": 8, "monkeys": 12}
animals_in_zoo["dinosaurs"] =  0
print(animals_in_zoo)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
menu["cheesecake"] = 8
print(menu)

animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 1}
print(animals_in_zoo)
print()

#Example 6
print("Example 6")
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
print()

#Example 7
print("Example 7")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"}) #add a new key word and value
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight" #change the value of key word
print(oscar_winners)
oscar_winners["Animated Feature"] = "Shrek"
print(oscar_winners)
print()

#Example 8 
print("Example 8")
drinks = ["Espresso", "Chai", "Decaf", "Drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)

zipped_drinks_2 = zip(caffeine, drinks)
drinks_to_caffeine_2 = {key: value for key, value in zipped_drinks_2}
print(drinks_to_caffeine_2)
print()
