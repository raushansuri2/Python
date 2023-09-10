#print("Enter the name");


#user_text = input('enter nnameeee');
#user_text.capitalize()
#user_text.title()
#print("Enter the name:",user_text.capitalize());

ranking = ['John', 'Sen', 'Lisa']
for index, item in enumerate(ranking):
    print(index, item)
    row = f"{index} this is key and item {item}"
    print(row)

rank = input('Enter a name')
print(ranking.index(rank))

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
print(seconds)

names = ["john smith", "jay santi", "eva kuki"]

# new code
new_name = [name.title() for name in names]
print(new_name)

# new code
usernames = ["john 1990", "alberta1970", "magnola2000"]
new_name = [len(name) for name in usernames]
print(new_name)

#New Program
user_entries = ['10', '19.1', '20']
new_name = [float(name) for name in user_entries]
total = sum(new_name)
print(total)


try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    per = (value/total_value) * 100;
    message = f"That is{per}%"
    print(message)
except:
    message = f"Enter total value: {total_value}\n"
    print(message)
    message = f"Enter value: {value}"
    print(message)
    message = f"You need to enter a number. Run the program again."
    print(message)
