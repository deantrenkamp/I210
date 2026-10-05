meeting = {}

while True:
    name = input("Please enter a person's name to add or remove them from the meeting (or "" to exit): ")
    if name == "":
        break
    elif name in meeting:
        in_meeting = input(f"{name} is currently in the meeting - would you like to remove them (Y/N)? ")
        if in_meeting == "N":
            print(f"{name} was not removed.")
        elif in_meeting == "Y":
            del meeting[name]
            continue
    meal_preference = input(f"Is {name} Vegitarian (Y/N or "" to cancel)? ")
    if meal_preference == "":
        print(f"{name} was not added.")
    
    meeting[name] = meal_preference




print("Meeting Information Summary\n")
print("-----------------------------\n")
print(f"The total amount of guests is: {len(meeting)}\n")
print(f"\nVegetarian Guests: ")
if "Y" in meeting.values():
    for i in meeting.keys():
        if meeting[i] == "Y":
            print(i)
else:
    print("None Currently")

print(f"\nNon_Vegetarian Guests: ")
if "N" in meeting.values():
    for i in meeting.keys():
        if meeting[i] == "N":
            print(i)
else:
    print("None Currently")


   



