print("Welcome to My Computer Quiz")
playing = input("Do you want to Play?  ")
if playing.lower() != "yes":
    quit()
print("Okay Let's Play :)")
score = 0
question = 0
answer = input("Who is the current goat of football?  ")
if answer.lower() == "messi":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1
answer = input("Which team won the uefa in 2021? ")
if answer.lower() == "chelsea":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1

answer = input("Who is the current striker of PSG?  ")
if answer.lower() == "mbappe":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1

answer = input(
    "Which chelsea stricker is currently injured in chelsea and is costing the team losses?  ")
if answer.lower() == "nkunku":
    print("correct !")
    score += 1
else:
    print("Incorrect !")

question += 1

answer = input("Which stricker is also called penaldo?   ")
if answer.lower() == "ronaldo":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1


answer = input(
    "Which club has spent more money on players and still have a losing streak?   ")
if answer.lower() == "chelsea":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1


answer = input("Which club has more aggressive fans than players ?   ")
if answer.lower() == "manchester united":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1


answer = input("Which player had his girlfriend stolen by a goalkeeper?   ")
if answer.lower() == "kevin de bryne":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1


answer = input("Which club won the trebble?   ")
if answer.lower() == "manchester city":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1

answer = input("Which team is said to be currently cooking this season?   ")
if answer.lower() == "tottenhum":
    print("correct !")
    score += 1
else:
    print("Incorrect !")
question += 1

print("You have done " + str(question) + " questions")

print("Your have scored " + str(score/question * 100) + "%")
