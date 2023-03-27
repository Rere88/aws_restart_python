print("hello,world!")

name = input("give me your name: ")
print("your name is " + name)

age = int(input("Enter your age: "))

print("were" + "wolf")
print ("4"+ "chan")
print(str(4) + "chan")
print(4 * "test")

name = ("John Smith")
age = 20
new_patient = True 

name = input("what is your name: ")
print ("Hi, " + name )

age = input("Enter your age: ")
print ("I am " + age)

colour = input("what is your favouritebl colour? ")
print ("My favourite colour is "  + colour)

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("Guess:  "))
  guess_count += 1
if guess == secret_number:
 print("you won!")
Break
else
  print(“You failed!”)