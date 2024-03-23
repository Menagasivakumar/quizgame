player=input("Do you want to play:")
if (player.lower()!="yes"):
    quit()
print("okay, lets play")
score=0

question=input("Which animal is known as the 'Ship of the Desert'?")
if question.lower()=="camel":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("How many days are there in a week?")
if question.lower()=="seven":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("How many hours are there in a day?")
if question.lower()=="24":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("Which animal is known as the king of the jungle?")
if question.lower()=="lion":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("Name the National animal of India?")
if question.lower()=="tiger":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("What is the capital of India?")
if question.lower()=="new delhi":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("Name the biggest continent in the world?")
if question.lower()=="asia":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("Name the house made of ice?")
if question.lower()=="igloo":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("Sun rises in the....")
if question.lower()=="east":
    print("correct")
    score += 1
else:
    print("incorrect")
question=input("How many sides are there in a triangle?")
if question.lower()=="three":
    print("correct")
    score += 1
else:
    print("incorrect")
print("your score is ",score)