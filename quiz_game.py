print("Welcome to Summoner's Quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's destroy the enemies Nexus!")
score = 0
answer = input("What is the name of the continent where the city of Demacia and Noxus are located? ")
if answer.lower() == "valoran":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which champion's weapon of choice is a rocket launcher? ")
if answer.lower() == "jinx":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who is the only champion that can truly revive another champion? ")
if answer.lower() == "zilean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which champion yells 'DEMACIA!' as he charges into battle? ")
if answer.lower() == "garen":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who is the Undead Juggernaut? ")
if answer.lower() == "sion":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which two champions are famously known as the 'Bird and the Branch'? ")
if answer.lower() == "xayah and rakan":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the name of the river that runs through the center of Summoner's Rift? ")
if answer.lower() == "the serpentine river":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Which champion is known as the 'Chain Warden'? ")
if answer.lower() == "thresh":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the name of Yasuo's brother? ")
if answer.lower() == "yone":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Who was the first champion ever designed? ")
if answer.lower() == "singed":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
if score >= 8:
    print("You demolish the nexus!")
elif score >= 5:
    print("Nexus got damaged! It was close")
else:
    print("Not even close, more luck next time!")
