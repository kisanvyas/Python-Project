#this program says Welcome and calculate your age

print("What is your name ?")
myName = input()
print ("                       Welcome " + myName)

print(" Enter present year : ")
presentYear = int(input())
print(" Enter your birth year: ")
birthYear = int(input())
age = (presentYear - birthYear)
print("You are " + str(age) + " years old now." )

if(age<18) :
    print("Sorry, You are not eligible for votting.")
else:
    print("Congrats !! you will be a voter.")
