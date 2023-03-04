# Assignment One
name = "Osama"
age = "38"
country = "Egypt"

print(f"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt


# Assignment Two
print(f"Hello '{name}', How You Doing \\\n \"\"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country}")


# Assignment Three
name1 = 'Elzero'

print(f"Second Letter Is \"{name1[1:2]}\"")
print(f"Third Letter Is \"{name1[2:3]}\"")
print(f"Last Letter Is \"{name1[len(name1) - 1]}\"")
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"


# Assignment Four
print(name1[1:4])  # lze
print(f"{name1[0]}{name1[2]}{name1[4]}")  # Ezr
print(f"{name1[4]}{name1[2]}{name1[0]}")  # rzE

# Needed Output
# "lze"
# "Ezr"
# "rzE"


# Assignment Five
name2 = "#@#@Elzero#@#@"
print(name2.strip("#@"))
# Needed Output
# Elzero


# Assignment six
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500


# Assignment Seven
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero


# Assignment Eight
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())
# Needed Output
# osAMa
# OSAma


# Assignment Nine
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

# Needed Output
# 2


# Assignment Ten
name = "Elzero"

print(name.find("z"))

# Needed Output
# 2

# Assignment Eleven
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))

# Needed Output
# I Love Python And Although <3 Elzero Web School


# Assignment Twelve
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love"))

# Needed Output
# I Love Python And Although Love Elzero Web School


# Assignment Thirteen
name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
