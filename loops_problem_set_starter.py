
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# # Write a for loop that prints out each character in the above "word" variable
# for char in word:
#     print(f"The char {char}")

# Write a while loop that does the same thing!
# count=0
# char_len= len(word)
# while (count < char_len):
#     print(word[count])
#     count+=1
    
# print(char_len)
    

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
# start=100
# end=140
# while(end >start):
#     if(start%2==0):
#         print(f"{start} is Even Number")
#     start+=1;





# Write a for loop that does the same thing (with range())
# for count in range(100,141):
#     if(count%2==0):
#         print(f"{count} is Even Number.")





#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
word=input("Type 'sillygoose' to end\n")
while(word!="sillygoose"):
    word=input("Type 'sillygoose' to end\n")
    print(f"You type {word}")