fruits = ["apple", "banana", "cherry"]
name1 = "john"  # string
age = 5  # int
is_male = True  # bool
for x in fruits:
    print(x)
else:
    print("\n" + "abc")  # "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.
    print(name1 + " abc", end='')  # extra argument to your print function that will tell the program that you don’t
    # want your next string to be on a new line
    print("defog")
    name1 = "jim"
    print(name1, age, is_male)
