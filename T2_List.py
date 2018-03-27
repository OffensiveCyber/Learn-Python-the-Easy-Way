cars = ['nissan', 'ford', 'honda','tesla', 'Volkswagen']

#print all cars name from the list
print cars[0]
print cars[1]
print cars[2]
print (cars[3].title())    #title() method displays word with first letter in caps

print "Hello " + cars[0] + ", What is your milage?"   #concetation demonstrated
print "Hello " + cars[1] + ", What is your milage?"
print "Hello " + (cars[2].title()) + ", What is your milage?"

cars.append('Ferrari')    #append to list
print "1"
print cars

cars[2] = "suzuki"     #3rd element from list is replaced
print "2"
print cars

cars.insert(2, 'honda') #Add new element in between the list
print "3"
print cars

del cars[3]            #delete item from list by its index number
print "4"
print cars

popped = cars.pop()    #removed last item from list but lets you work with it. 'popped' is just a variable here.
print "5"
print cars
print "Item removed from list is: " + popped

honda_comes_before = cars.pop(3) #popped middle item from list
print "6"
print cars
print "honda used to come before: " + honda_comes_before + " in list"
