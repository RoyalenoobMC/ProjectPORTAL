import random

print("1 = Number Guesser \n2 = Calculator \n3 = Grade Calculator\n4 = Random Password Generator")
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

if project == 2:
    var = input("Enter your equation: ")
    a = eval(var)
    print(a)

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
        print("L = Minimum, H = Highest\nDefault:")
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
        print("L = Minimum, H = Highest P = Plus M = Minus \nAdvanced:")
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
