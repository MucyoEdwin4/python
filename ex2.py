############### USER INPUT ############

# name = input('Enter your name here: ')

############### LISTS ############

countries = ['Rwanda','uganda','Kenya','Tanzania','Rwanda','Burundi','Morocco','Rwanda']
fruits = ['Avocado','banana','melon','passion']
numb = [3,5,2,8,7,1,6,4,9]
print(type(countries))
print(countries[2:])
print(countries[:2])
print(countries[0:3])
countries[6] = 'DRC'
print(countries[-1])                        # prints the last nth Element in the list
print(len(countries))                       # prints the total number of elements in the list
countries.extend(fruits)                    # it joins the second list to the first one
print(countries)
countries.append('South sudan')             # it adds or appends an element to the of the list
countries.insert(3,'Edwin')                 # it inserts an element before a specified index in the list
print(countries)
countries.remove('Edwin')                   # it removes an element from the list
print(countries)
indexNo = countries.index('Burundi')        # it checks the index of a given element inside a list
print(indexNo)
number = countries.count('Rwanda')          # it returns the number of times a given element appears in the list
print(number)
numb.sort()
print(numb)                                 # it sorts the list in the ascending order
print(fruits)
fruits.reverse()                            # it reverses the order of elements in the list
print(fruits)
numb2 = numb.copy()                         # it duplicates a list 
print(numb2)  
numb2.pop()                                 # it removes (or pops out) the last element in the list                               
numb2.pop(2)                                 # it removes the element in the list with the specified index same as writting ( del numb2[2] )                             
print(numb2)

# numb2.clear() =! del numb2      (the clear method deletes every element from the list but the list remains to exist while the del removes everything the variable itself included )


########################### TUPLES ##############################

# A TUPLE IS SIMPLY AN IMMUTABLE LIST BUT INSTEAD OF USING SQUARE BRAQUETS [] WE USE PARANTHESIS ()

tuple1 = (3,'Hello', True, 4)
print(type(tuple1))


########################### FUNCTIONS ##############################
