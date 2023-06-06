import random
# personal details
age = random.randint(16,42)



# attributes
height = random.randint(1, 100)
strength = random.randint(1, 100)
speed = random.randint(1, 100)
jump = random.randint(1, 100)
endurance = random.randint(1, 100)
inside = random.randint(1, 100)
dunk = random.randint(1, 100)
midrange = random.randint(1, 100)
threepointer = random.randint(1, 100)
freethrow = random.randint(1, 100)
offensiveiq = random.randint(1, 100)
defensiveiq = random.randint(1, 100)
dribbling = random.randint(1, 100)
passing = random.randint(1, 100)
rebounding = random.randint(1, 100)

# names
first_names = ('John', 'David', 'Michael', 'Daniel', 'Matthew', 'Andrew', 'William', 'James', 'Joseph', 'Christopher', 'Benjamin', 'Samuel', 'Henry', 'Jackson', 'Ethan', 'Anthony', 'Joshua', 'Ryan', 'Thomas', 'Jonathan', 'Nicholas', 'Alexander', 'Nathan', 'Jacob', 'Daniel', 'Tyler', 'Brandon', 'Christian', 'Jose', 'Zachary', 'Logan', 'Kevin', 'Caleb', 'Jonathan', 'Justin', 'Aaron', 'Eric', 'Jason', 'Kyle', 'Adam', 'Brian', 'Timothy', 'Steven', 'Mark', 'Jeremy', 'Alex', 'Charles', 'Sean', 'Patrick', 'Travis')
last_names = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins')
name =" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(1))


overall = height + strength + speed + jump + endurance +inside + dunk + midrange + threepointer + freethrow + offensiveiq + defensiveiq  + dribbling +passing +rebounding

# 85+: All-time great
# 75+: MVP candidate
# 65+: All League candidate
# 55+: Starter
# 45+: Role player
# lower: Bad player

cm = random.randint(184, 225)
inches = float(cm) / 2.54
feet = int(inches) // 12
remaining_inches = round(inches % 12, 2)
truehgt = str(feet) + " Feet " + str(remaining_inches) + " Inches "



if cm >= 213 and cm < 225:
    weight = random.randint(118, 127)
elif cm >= 204 and cm < 210:
    weight = random.randint(109, 118)
elif cm >= 198 and cm < 203:
    weight = random.randint(100, 109)
elif cm >= 191 and cm < 198:
     weight = random.randint(91, 100)
elif cm >= 183 and cm < 191:
    weight = random.randint(82, 91)
else:
    weight = 0




if cm >= 209:
    position = "PF"
elif cm >= 206:
    position = "SF"
elif cm >= 200:
    position = "SG"
elif cm >= 195:
    position = "PG"
else:
    position = "C"
