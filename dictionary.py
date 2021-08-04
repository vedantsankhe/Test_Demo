#dictionary
dict= {1: "hello", 2: "World",3: "Apple", 4: "ball"}

#square dict
square_dict = {num: num*num for num in range(1, 20)}
print(square_dict)

# Creating a Dictionary 
# with Integer Keys
Dict = {1: 'Hey', 2: 'Hello', 3: 'Hi'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary 
# with Mixed keys
Dict = {'Name': 'OK', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Hey'
Dict[2] = 'Hello'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

#
D = {'spam': 2, 'ham': 1, 'eggs': 3}
D['spam']
len (D)
#D['ham'] = ['grill', 'bake', 'fry']
(D.keys())
#del D['eggs']
#list(D.values())
#list(D.items())
D.pop('ham')
D