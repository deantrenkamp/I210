attendees = ["Amari McIntyre", "Ray Lowe", "Anna Hopkins", "Oaklynn Duran", "Flor Himenez"]
speakers = ["Ray Lowe", "Flor Himenez"]

i = 0
print('The following people are attending the conference: ')
while i < len(attendees):
    print(f'\t {attendees[i]}')
    i += 1

name = input("Please enter a person's name: ")

if name in speakers:
    print("That person is attending the conference and they are a speaker.")
elif name in attendees:
    print("That person is attending the conference.")
else:
    print("That person isn't currently on the conference list.")
    new_attendee = input("Would you like to add them (Y/N)? ")
    if new_attendee == 'Y':
        print(f"{name} has been added to the attendees list.")
        new_speaker = input("Are they also a speaker (Y/N)? ")
        if new_speaker == 'Y':
            print(f"{name} has been added to the speakers list.")
            print("The conference is now full!")
        else:
            print("The conference is now full!")
    else:
        print(f"One more person could still attend.")





    




