#Rough Draft Attendance System for After School

import random

present = []
absent = []
classlist = ["Test", "Real", "Student", "Totally", "Not", "Fake"]

print("Hello! It's a brand new day! Let's take Attendance.")


done = False #generic placeholder
print("Here's the class list, let's go through and see who's present and who's absent.")
while not done:
    print(classlist)
    student = random.choice(classlist)
    print("Is", student, "here?")
    ans = input("Yes or No: ")
    if ans == "yes" or ans == "Yes":
        print("Cool, let's move on to the next student.")
        present.append(student)
        classlist.remove(student)
    elif ans == "no" or ans == "No":
        print("I see, that's unfortunate. Let's try the next student.")
        absent.append(student)
        classlist.remove(student)
    else:
        print("It's a yes or no question! Try again.")
    if not classlist: #This particular line of code is debatable.
        done = True
    
print("Oh! Looks like we're all outta students. Let's see the results.")
print("The students that are here today are:", present)
print("The students that aren't here today are:", absent)
