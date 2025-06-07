from sys import argv  #This is how you add features to your script from the Python feature set
#The argv is the ”argument variable", This variable holds the arguments you pass to your Python script when you run it.
script, first, second, third = argv # rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third

print("the script is called:", script)
print("the first variable is called:", first)
print("the second variable is called:", second)
print("the third variable is called:", third)
