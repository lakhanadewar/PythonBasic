# # While Loops

# # count= 0
# # while count <=10:
# #     print(' *' * count)
# #     count+=1

    
# # Snake Eye Script
# # 
# import random

# roll1=random.randint(1,6)
# roll2=random.randint(1,6)
# roll_count=1

# while roll1!=1 or roll2!=1:
#     print(f'{roll1}  {roll2}')
#     roll1=random.randint(1,6)
#     roll2=random.randint(1,6)
#     roll_count+=1

# print(f"Snake Eye at {roll_count} for {roll1} and {roll2}")


# For Loop

# for num in range(12):
#     if num%2!=0:
#         print(num)

# Poem in For loop
count=100
for num in range(101):
    remain=count-num
    if remain !=0:
        print(f"{remain} on Wall, {num} given, {remain} remains ")
    else:
        print("No Bottle Remaining")