monthConversions = {
    "Jan": "January",  # Key : value
    "Feb": "February",  # all keys must be unique
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    6: "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions)  # print dictionary
print(monthConversions["Mar"])  # March
print(monthConversions.get("Dec"))  # December
print(monthConversions.get("Luv"))  # None
print(monthConversions.get("Luv", "Love"))  # Love
del monthConversions[6]  # Deleting a specific key 6
print(monthConversions)
pop_ele = monthConversions.pop("Feb")  # pop feb
print(pop_ele)  # February
pop_ele1 = monthConversions.popitem()  # pop last item in dictionary
print(pop_ele1)  # ('Dec', 'December')
