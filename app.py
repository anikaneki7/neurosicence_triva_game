import sys
import random  # randomizing
import time  # For a slight delay in responses

# this is the format for range - range(start, stop (exclusive), step)


def timer(number):

    time.sleep(1)

    print(f"The showcase will begin in {number} seconds⏳")

    time.sleep(1)

    for t in range(number, 0, -1):
        # this is the format for range - range(start, stop (exclusive), step)
        print(t)

        time.sleep(1)

    print("🎬 The showcase has begun! 🚀")


timer(3)

time.sleep(1)

print("🧠 Welcome to the Brain Trivia Game!")

time.sleep(1)

print("Test your neuroscience knowledge by answering the following questions")

time.sleep(1)

start = input("Press SPACEBAR and then ENTER to start please: ")

if start == " ":  # If the user presses the SPACEBAR once and then ENTER, start will store a single space character " "

    time.sleep(1)

    print("Game starting...🎮")

    time.sleep(1)

    def score(actual_score):
        print(f"Your current score is {actual_score}")

    time.sleep(1)

    print("You will get one point for every question you get correct!")

    # the question only pops up if correct input was given

    score = 0  # Initialize score

    time.sleep(1.25)

    print("What is the term for the ability of the brain to reorganize itself by forming new neural connections?")
    print("A) Neurogenesis")
    print("B) Synaptogenesis")
    print("C) Neural plasticity")
    print("D) Long-term potentiation")

    # the use of while-loop/validation loop

    while True:
        answer = input(
            "Choose the correct answer (A, B, C, D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("⚠️ Invalid input! Please enter A, B, C, or D.")

    # The strip() method removes any leading (before the text) and trailing (after the text) spaces.
    # The upper() method converts lowercase letters to uppercase, ensuring that the input is case insensitive.

    if answer == "A":
        print("That is the correct answer✅")
        score += 1  # Increase score
    else:
        print("❌Incorrect! Looks like your neurons misfired on that one⚡")
        print("The correct answer is A")
else:
    print("Oh no! You forgot to press the SPACEBAR first🧐")
    sys.exit()

questions = [
    ["What rare condition causes a person to believe their loved ones have been replaced by impostors?",
     "A) Cotard's Delusion",
     "B) Capgras Syndrome",
     "C) Alice in Wonderland Syndrome",
     "D) Prosopagnosia",
     "B"],

    ["Which part of the brain is responsible for generating dreams during REM sleep?",
     "A) Hippocampus",
     "B) Pons",
     "C) Amygdala",
     "D) Thalamus",
     "B"],

    ["Which phenomenon causes a person to feel a missing limb as if it is still there?",
     "A) Mirror-touch synesthesia",
     "B) Phantom limb syndrome",
     "C) Alien hand syndrome",
     "D) Hemispatial neglect",
     "B"],

    ["What is the name of the brain network that activates when a person is at rest and not focused on external tasks?",
     "A) Salience network",
     "B) Executive control network",
     "C) Default mode network",
     "D) Dorsal attention network",
     "C"],

    ["Which neurotransmitter is most strongly linked to the experience of déjà vu?",
     "A) Dopamine",
     "B) Acetylcholine",
     "C) Serotonin",
     "D) Glutamate",
     "D"]
]

random.shuffle(questions)
# use random.shuffle when its a list of choices to shuffle the list randomly

time.sleep(1)

score = 0  # Initialize score

for q in questions:

    # just a random variable 'q' due to the context
    # Print the question q[0] is the first object in the list

    print("🧠 " + q[0])  # Print the question
    print(q[1])  # Option A
    print(q[2])  # Option B
    print(q[3])  # Option C
    print(q[4])  # Option D

    # the use of while-loop/validation loop

    while True:
        answer = input(
            "Choose the correct answer (A, B, C, D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("⚠️ Invalid input! Please enter A, B, C, or D.")

    if answer == q[5]:
        print("That is the correct answer✅")
        score += 1  # Increase score
    else:
        print(f"❌ Incorrect! Looks like the correct answer was {q[5]}🧑‍🏫")

    time.sleep(0.5)

    print(f"\n🎯 Your score: {score}/{len(questions)}")

time.sleep(1)

print(f"\n🎯 Final Score: {score}/{len(questions)}")

# time.sleep() used after each segment to delay reading of next line improving experience
# # f-formatting to prevent certain variables inside "" to be treated as literal string value

time.sleep(1)

if score == len(questions):
    print("\n🥳 Amazing! You are a brain expert!")
elif score >= 3:
    print("\n👍 Good job! You know a lot about the brain!")
else:
    print("\n😕 Keep studying! The brain is fascinating!")
