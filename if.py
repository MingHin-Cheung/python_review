is_male = True
is_tall = True

is_tall = input("are you tall? Y/N")

if is_tall == "Y" or is_tall == "y":
    is_tall = True
else:
    is_tall = False

is_male = input("What is your gender? M/F")

if is_male == "M" or is_male == "m":
    is_male = True
else:
    is_male = False

if is_male and is_tall:
    print("you're a tall male")
elif is_male and not is_tall:
    print("you're a short male")
elif not is_male and is_tall:
    print("you're a tall female")
else:
    print("you're a short female")
