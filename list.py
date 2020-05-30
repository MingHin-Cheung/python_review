food = ["pizza", "sushi", "burger"]
nums = [1, 2, 3, 10, 20]

print(food)  # print list
print(food[1])  # pizza
print(food[-1])  # burger
print(food[1:])  # start at position 1
print(food[1:2])  # start at position 1,up to 2 but not include

food[1] = "pasta"
print(food)
food.extend(nums)  # combine 2 lists
print(food)
food.append("bacon")
print(food)
food.insert(1, "rice")
print(food)
food.remove(10)
print(food)
food.pop()
print(food)  # remove the last element of the list
print(food.index("rice"))    # check rice position
print(food.count("rice"))    # check rice counts
food = ["pizza", "sushi", "burger"]
food.sort() # sort list
print(food)
nums.reverse()
print(nums)
num2 = nums.copy() #copy the list
food.clear()    #delete everything in the list