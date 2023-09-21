#Excercise 1
print("Excercise 1")
my_dictionary = {"song": "Estranged","artist": "Gun's and Roses"}
print(my_dictionary)
my_dictionary["song"] = "Paradise city"
print(my_dictionary["song"])
print()

#Excercise 2
print("Excercise 2")
print({"name": "Victor"}.get("name"))
print({"name": "Victor"}.get("nickname", "nickname is not a key"))
print()

#Excercise 3
print("Excercise 3")
dictionary = {
	1: 'hello',
	'two': True,
	'3':[1, 2, 3],
	'Four': {'fun': 'addition'},
	5.0: 5.5
}
print(dictionary)
print()

#Excercise 4
print("Excercise 4")
dict1 = {'color': 'blue', 'shape':'circle'}
dict2 = {'color': 'red', 'number': 42}
print(dict1,dict2)
dict1.update(dict2)
print(dict1)
print()

#Excercise 5
print("Excercise 5")
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}
print(ex_dict.keys())
print(ex_dict.values())
print(ex_dict.items())
print()

#Excercise 6 
print("Excercise 6, crear archivos .txt, leer, escribir y añadir")
