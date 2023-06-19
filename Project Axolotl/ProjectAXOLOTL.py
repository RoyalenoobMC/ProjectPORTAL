import random

print(
    "1: Number Guesser \n2: Calculator \n3: Grade Calculator\n4: Random Password Generator\n5: Luck Games\n6: Hangman")
project = int(input("What project would you like to open: "))

if project == 1:
    mn = int(input("Enter the max number: "))

    ri = random.randint(0, mn)

    while True:
        guess = int(input("Enter guess: "))
        if guess < ri:
            print("More")
        if guess > ri:
            print("Less")
        if guess == ri:
            print("Perfect")
            break
    print("1: Yes\n2: No")
    again = int(input("Would you like to play again: "))
    while again == 1:
        mn = int(input("Enter the max number: "))

        ri = random.randint(0, mn)

        while True:
            guess = int(input("Enter guess: "))
            if guess < ri:
                print("More")
            if guess > ri:
                print("Less")
            if guess == ri:
                print("Perfect")
                break
        print("1: Yes\n2: No")
        again = int(input("Would you like to play again: "))
if project == 2:
    var = input("Enter your equation: ")
    x = eval(var)
    print(x)
    print("1: Yes\n2: No")
    again = int(input("Would you like to use the calculator again?"))
    while again == 1:
        var = input("Enter your equation: ")
        x = eval(var)
        print(x)
        print("1: Yes\n2: No")
        again = int(input("Would you like to use it again?"))

if project == 3:
    ns = {}
    default = {
        "AL": 90,
        "AH": 100,
        "BL": 80,
        "BH": 89,
        "CL": 70,
        "CH": 79,
        "DL": 60,
        "DH": 69,
        "FH": 59,
        "FL": 0
    }
    ad = {
        "APH": 100,
        "APL": 97,
        "AH": 96,
        "AL": 93,
        "AMH": 92,
        "AML": 90,
        "BPH": 89,
        "BPL": 87,
        "BH": 86,
        "BL": 83,
        "BMH": 82,
        "BML": 80,
        "CPH": 79,
        "CPL": 77,
        "CH": 76,
        "CL": 73,
        "CMH": 72,
        "CML": 70,
        "DPH": 69,
        "DPL": 67,
        "DH": 66,
        "DL": 65,
        "DMH": 65,
        "DML": 60,
        "FH": 59
    }

    print("DISCLAIMER: The maximum score is one hundred, and the conversion ranges cannot be changed.")

    print("1 = Simple\n2 = Advanced")
    mode = int(input("What mode would you like: "))

    if mode == 1:
        students = int(input("How many students do you have: "))
        q = int(input("How many questions are there: "))
        print("L: Minimum, H: Highest\nDefault:")
        print(default)

        for x in range(1, students + 1):
            ts = 0
            name = input("What is the student's name: ")
            entry = f"{x}. {name}"

            for y in range(1, q + 1):
                qs = int(input(f"What is the score for Question {y}: "))
                ts += qs

                if 90 <= ts <= 100:
                    grade = "A"
                elif 80 <= ts <= 89:
                    grade = "B"
                elif 70 <= ts <= 79:
                    grade = "C"
                elif 60 <= ts <= 69:
                    grade = "D"
                elif 0 <= ts <= 59:
                    grade = "F"
                else:
                    print("ERROR: Score is out of range.")
                    exit()

                if y == q:
                    print(name + ": " + grade + " " + str(ts))

            ns[entry] = f"{ts} {grade}"
        print(ns)

    if mode == 2:
        students = int(input("How many students do you have: "))
        q = int(input("How many questions are there: "))
        print("L: Minimum, H: Highest P: Plus M: Minus \nAdvanced:")
        print(ad)

        for x in range(1, students + 1):
            ts = 0
            name = input("What is the student's name: ")
            entry = f"{x}. {name}"

            for y in range(1, q + 1):
                qs = int(input(f"What is the score for Question {y}: "))
                ts += qs

                if 97 <= ts <= 100:
                    grade = "A+"
                elif 93 <= ts <= 96:
                    grade = "A"
                elif 90 <= ts <= 92:
                    grade = "A-"
                elif 87 <= ts <= 89:
                    grade = "B+"
                elif 83 <= ts <= 86:
                    grade = "B"
                elif 80 <= ts <= 82:
                    grade = "B-"
                elif 77 <= ts <= 79:
                    grade = "C+"
                elif 73 <= ts <= 76:
                    grade = "C"
                elif 70 <= ts <= 72:
                    grade = "C-"
                elif 67 <= ts <= 69:
                    grade = "D+"
                elif 65 <= ts <= 66:
                    grade = "D"
                elif 60 <= ts <= 64:
                    grade = "D-"
                elif 0 <= ts <= 59:
                    grade = "F"
                else:
                    print("ERROR: Score is out of range.")
                    exit()
                if y == q:
                    print(name + ": " + grade + " " + str(ts))
            ns[entry] = f"{ts} {grade}"
        print(ns)

if project == 4:
    var = int(input("Enter max amount characters: "))
    password = ""
    for i in range(var):
        password += chr(random.randint(33, 126))

    print("Password: " + password)

if project == 5:
    ld = []
    counts = {}
    counts2 = {}
    print("1: Coin Flip\n2: Dice Game")
    lgc = int(input("What luck game would you like to play: "))

    if lgc == 1:
        cf = random.randint(0, 2)

        if cf == 1:
            print("Heads")
            ld.append(1)
        else:
            print("Tails")
            ld.append(2)

        print("1: Yes\n2: No")
        again = int(input("Would you like to go again: "))

        while again == 1:
            cf2 = random.randint(0, 2)
            ld.append(cf2)
            if cf2 == 1:
                print("Heads")
            else:
                print("Tails")
            print("1: Yes\n2: No")
            again = int(input("Would you like to go again: "))

            if again == 2:
                break

        mean = sum(ld) / len(ld)
        for num in ld:
            counts[num] = counts.get(num, 0) - 1

        mode = max(counts, key=counts.get)
        if mode == 1:
            mode2 = "Heads"
        else:
            mode2 = "Tails"

        print("For the Mean: 1 is tails and 0 is heads.")
        print("Mean(Average): " + str(mean) + "\nMode(Most Frequent): " + mode2)

    if lgc == 2:

        print("Game is in development. Some cube rolls might not work.")

        rd = random.randint(1, 7)
        ld = []
        count = {}
        count2 = {}
        ld.append(rd)

        if rd == 1:
            print("\n   ●\n")
        if rd == 2:
            print("●\n\n      ●")
        if rd == 3:
            print("       ●\n   ●\n●")
        if rd == 4:
            print("●     ●\n\n●     ●")
        if rd == 5:
            print("●     ●\n   ●\n●     ●")
        if rd == 6:
            print("●  ●  ●\n\n●  ●  ●")

        print("1: Yes\n2: No")
        again = int(input("Would you like to play again: "))

        while again == 1:
            rd2 = random.randint(1, 7)
            ld.append(rd2)
            if rd2 == 1:
                print("\n   ●\n")
            if rd2 == 2:
                print("●\n\n      ●")
            if rd2 == 3:
                print("     ●\n   ●\n●")
            if rd2 == 4:
                print("●     ●\n\n●     ●")
            if rd2 == 5:
                print("●     ●\n   ●\n●     ●")
            if rd2 == 6:
                print("●  ●  ●\n\n●  ●  ●")

            print("1: Yes\n2: No")
            again = int(input("Would you like to play again: "))

            if again == 2:
                break

        mean = sum(ld) / len(ld)
        for num in ld:
            counts[num] = counts.get(num, 0) + 1

        mode = max(counts, key=counts.get)
        print("Mean(Average): " + str(mean))
        print("Mode(Most Frequent):")

        if mode == 1:
            print("\n   ●\n")
        if mode == 2:
            print("●\n\n      ●")
        if mode == 3:
            print("     ●\n   ●\n●")
        if mode == 4:
            print("●     ●\n\n●     ●")
        if mode == 5:
            print("●     ●\n   ●\n●     ●")
        if mode == 6:
            print("●  ●  ●\n\n●  ●  ●")
        exit()

if project == 6:
    print("Game is in development. Some cube rolls might not work.\n")
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    progress = []
    correct = 1

    print("1: Unlimited\n2: Limited")
    mode = int(input("Which mode would you like: "))

    if mode == 1:
        word = str(input("Think of a word: "))
        wlength = int(input("How many letters is it: "))

        characters = list(word)

        for char in range(0, wlength):
            progress.append("_")

        while correct != wlength:
            letter = random.randint(0, 25)
            index = characters.index(letter)

            print("\nThis is my guess " + letters[letter])

            print("1: Yes\n2: No")
            correction = int(input("Is that correct: "))
            if correction == 1:
                progress[index] = letters[letter]
                correct += 1
                print(correct)
            if correct == wlength:
                print("I have won! Good luck next time!")

    if mode == 2:
        word = str(input("Think of a word: "))
        wlength = int(input("How many letters is it: "))
        numtries = int(input("How many guesses: "))
        characters = list(word)

        for char in range(0, wlength):
            progress.append("_")

        for x in range(0, numtries):
            letter = random.randint(0, 25)

            print("This is my guess " + letters[letter])

            print("1: Yes\n 2: No")
            correction = int(input("Is that correct: "))
            if correction == 1:
                index = characters.index(letter)
                progress[index] = letter
                correct += 1
                print(correct)
            if correct == wlength:
                print("I won! Good luck next time!")
        print("You won! Great job!")
