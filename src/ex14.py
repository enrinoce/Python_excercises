from sys import argv

script, user_name = argv
prompt ='>' #ogni volta che mi chiede l'input per likes, lives etc. mi mette la freccetta perchè prompt è un oggetto con '>' come stringa al suo interno

print(f"Hi, {user_name}, I'm the {script} script.") #crea una f-string, che permette di inserire variabili ed espressioni all'interno di una stringa
print("I'd like to ask you a feew questions.")
print(f"Do you like me {user_name}?")
likes= input(prompt)

print(f"Where do you live? {user_name}")
lives= input(prompt)

print("Which computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes}, about liking me.
    You live in {lives}. Not sure where that is.
      And you have a {computer} computer. Nice.
      """)
