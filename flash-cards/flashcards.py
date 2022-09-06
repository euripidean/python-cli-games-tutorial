#import
import json

#functions
def read_data(file_path):
    with open(file_path, 'r') as f:
        global data 
        data = json.load(f)

def print_design():
    print('*' * 50)

def start_message():
    print("Let's test your geographical knowledge!")

def end_message(score):
    if score == 5:
        print("Amazing work, you got them all right!")
    elif score > 2.5:
        print("Close! You're almost there.")
    else:
        print("You'd better play again and have a practice!")

#game
file_path = 'flash-cards/me-capitals.json'
read_data(file_path)

# initialize scoreboard
total = len(data["cards"])
# # initialize score as 0
score = 0

print_design()
start_message()
print_design()

for i in data["cards"]:
    guess = input(i["q"] + " > ")
if guess.lower() == i["a"].lower():
    score +=1
    print(f"Correct! Current score: {score}/{total}")
else:
    print("Incorrect! The correct answer was", i["a"])
    print(f"Current score: {score}/{total}")


print_design()
end_message(score)
print_design()