print('''
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \\ / _` |/ _ \\/ __|
   | | (_) | (_| | (_) \\__\\
   |_|\\___/ \\__,_|\\___/|___/
      
      ''')

item=[]
done_item=[]

def is_integer(value):
     try:
          int(value)
          return True
     except ValueError:
          return False

while True:    
    for idx in range(len(item)):
        print(f"{idx+1}. {item[idx]}")
    reply=input("Enter a command. Type 'h' for help: ")
        
    if reply=='h':
            print('''***TODO LIST HELP***\nType 'q' to quit\nTo add a todo to the list, type it and hit enter\nTo complete a todo enter its number\n''')
    elif reply=='q':
        break
    elif is_integer(reply):
         if int(reply) <= len(item):
            done=item.pop(int(reply)-1)
            done_item.append(done)
         else:
              print("*"*30)
              print("No Iteam  found in the ToDo List")
    else:
        item.append(reply)
        
            
    print("*"*30)

print(f"You have completed {len(done_item)}")
for id in range(len(done_item)):
     print(f"{id+1}. {done_item[id]}")