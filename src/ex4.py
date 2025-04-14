cars= 100 #number of total cars available
space_in_a_car= 4.0 #How may people can you fit into a car
drivers=30  #Number of drivers
passengers= 90  #People that need a drive
cars_not_driven= cars - drivers 
cars_driven= drivers
carpool_capacity= cars_driven * space_in_a_car
average_driver_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people, today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_driver_per_car, "in each car")