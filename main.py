name =input("what is ur name?")
print("\nwelcome to the adventure,"   + name)
print("\nyou are standing at the entrance of a dark cave\n")
choice1= input("do you want to enter?(type 'yes' or 'no'):")
if choice1 =='yes':
    print("\nyou step inside and you hear a loud growl!\n")
    choice2=input("do you pick up 'sword' or open the 'chest'?")
    if choice2== "sword":
     print("\na huge monster eats you alive! Game Over")
    elif choice2 =="chest":
     print("\nyou open the chest and find bars of gold! Good ending, Game over")
else:
    print("\nyou are safe! easy ending game over")
