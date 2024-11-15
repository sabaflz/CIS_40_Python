# Ch.6, Ex.2
# Saba Feilizadeh
# This program handles a dictionary of friends I met in 2017 and 2018
# It allows the user to search for a friend, add a friend, and displays the lists of friends.

# Constant for the width of the line for the output
LINE_WIDTH = 50

# A dictionary of friends I met in 2017 and 2018
my_friends_dict = {
    "2017" : ["Jessica", "Sarah", "Ashkan", "Mina"],
    "2018" : ["Josh", "Gurpreet", "Nyi", "Carissa", "Josh", "Myra"],
}

# --------------------------------------------------------------------------
def find_friend():
    '''
    This function asks the user for a friend's name.
    It tells the user which year they met the friend.
    '''
    friend_name = input("Enter a friend's name to search for: ")

    if friend_name in my_friends_dict["2017"]:
        print(f"I met {friend_name} in 2017!")

    elif friend_name in my_friends_dict["2018"]:
        print(f"I met {friend_name} in 2018!")

    else:
        print(f"{friend_name} is NOT in my list of friends!")

    print("*" * LINE_WIDTH)
# --------------------------------------------------------------------------
def add_friend():
    '''
    This function asks the user for a friend's name and the year they were met.
    It adds the friend's name to the list of friends.
    '''
    friend_name = input("Enter a friend's name to add to the dictionary: ")

    year_met = input("Did you meet this friend in 2017 or 2018?\nEnter 1 for 2017 or 2 for 2018: ")

    if year_met == "1":
        my_friends_dict["2017"].append(friend_name)

    elif year_met == "2":
        my_friends_dict["2018"].append(friend_name)

    else:
        print("Invalid input!")

# --------------------------------------------------------------------------
def display_friends():
    '''
    This function displays the friends' names.
    '''
    print("*" * LINE_WIDTH)
    print("-" * (LINE_WIDTH // 2))

    print("The list of friends")

    print("-" * (LINE_WIDTH // 2))

    print(f"From 2017:\n{my_friends_dict["2017"]}")

    print(f"From 2018:\n{my_friends_dict["2018"]}")

    print("*" * LINE_WIDTH)

# --------------------------------------------------------------------------
def main():
    # Display the lists of friends from the dictionary (Original)
    display_friends()

    # Search for a friend in the dictionary (Ask user for a name)
    find_friend()

    # Add a friend to the dictionary (Ask user for a name)
    add_friend()

    # Display the lists of friends from the dictionary (Updated)
    display_friends()
    

# --------------------------------------------------------------------------
main()

print("Done!")

# --------------------------------------------------------------------------
'''
=============================================================
Output 1:
=============================================================
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina']
From 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Enter a friend's name to search for: Nyi
I met Nyi in 2018!
**************************************************
Enter a friend's name to add to the dictionary: Niloufar
Did you meet this friend in 2017 or 2018?
Enter 1 for 2017 or 2 for 2018: 1
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina', 'Niloufar']
From 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Done!

=============================================================
Output 2:
=============================================================
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina']
From 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Enter a friend's name to search for: George
George is NOT in my list of friends!
**************************************************
Enter a friend's name to add to the dictionary: Sam
Did you meet this friend in 2017 or 2018?
Enter 1 for 2017 or 2 for 2018: 2
**************************************************
-------------------------
The list of friends
-------------------------
From 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina']
From 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra', 'Sam']
**************************************************
Done!

'''