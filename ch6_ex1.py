# Ch.6, Ex.1
# Saba Feilizadeh
# This program handles a list of friends I met in 2017 and 2018
# It allows the user to search for a friend, add a friend, and display the lists of friends.

# Constant for the width of the line for the output
LINE_WIDTH = 50

# List of friends I met in 2017 and 2018
my_friends_list_2017 = ["Jessica", "Sarah", "Ashkan", "Mina"]
my_friends_list_2018 = ["Josh", "Gurpreet", "Nyi", "Carissa", "Josh", "Myra"]

# --------------------------------------------------------------------------
def concatenate_lists():
    '''
    This function concatenates the two lists of friends and displays the result.
    '''
    all_my_friends = my_friends_list_2017 + my_friends_list_2018

    print("-" * LINE_WIDTH)
    print(f"Here is the list of all my friends from 2017 and 2018:\n{all_my_friends}")
    print("-" * LINE_WIDTH)

# --------------------------------------------------------------------------
def find_friend():
    '''
    This function asks the user for a friend's name and takes two lists of friends as arguments.
    It prints a message if the friend name is in the list of friends.
    '''
    friend_name = input("Enter a friend's name to search for: ")

    if friend_name in my_friends_list_2017:
        print(f"I met {friend_name} in 2017!")

    elif friend_name in my_friends_list_2018:
        print(f"I met {friend_name} in 2018!")

    else:
        print(f"{friend_name} is NOT in my list of friends!")

    print("-" * LINE_WIDTH)
# --------------------------------------------------------------------------
def add_friend():
    '''
    This function asks the user for a friend's name and the year they were met.
    It appends the friend name to the list of friends.
    '''
    friend_name = input("Enter a friend's name to add to the list: ")

    year_met = input("Did you meet this friend in 2017 or 2018?\nEnter 1 for 2017 or 2 for 2018: ")

    if year_met == "1":
        my_friends_list_2017.append(friend_name)

    elif year_met == "2":
        my_friends_list_2018.append(friend_name)

    else:
        print("Invalid input!")

# --------------------------------------------------------------------------
def display_friends():
    '''
    This function displays the lists of friends.
    '''
    print("*" * LINE_WIDTH)

    print(f"The list of friends from 2017:\n{my_friends_list_2017}")

    print("-" * LINE_WIDTH)

    print(f"The list of friends from 2018:\n{my_friends_list_2018}")

    print("*" * LINE_WIDTH)

# --------------------------------------------------------------------------
def main():
    # Concatenate and Display the lists
    concatenate_lists()

    # Search for a friend in the list (Ask user for a name)
    find_friend()

    # Add a friend to the friends list (Ask user for a name)
    add_friend()

    # Display the lists of friends (Updated lists)
    display_friends()
    

# --------------------------------------------------------------------------
main()

print("Done!")

# --------------------------------------------------------------------------
'''
=============================================================
Output 1:
=============================================================
--------------------------------------------------
Here is the list of all my friends from 2017 and 2018:
['Jessica', 'Sarah', 'Ashkan', 'Mina', 'Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
--------------------------------------------------
Enter a friend's name to search for: Nyi
I met Nyi in 2018!
--------------------------------------------------
Enter a friend's name to add to the list: Niloufar
Did you meet this friend in 2017 or 2018?
Enter 1 for 2017 or 2 for 2018: 1
**************************************************
The list of friends from 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina', 'Niloufar']
--------------------------------------------------
The list of friends from 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
**************************************************
Done!

=============================================================
Output 2:
=============================================================
--------------------------------------------------
Here is the list of all my friends from 2017 and 2018:
['Jessica', 'Sarah', 'Ashkan', 'Mina', 'Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra']
--------------------------------------------------
Enter a friend's name to search for: George
George is NOT in my list of friends!
--------------------------------------------------
Enter a friend's name to add to the list: Sam
Did you meet this friend in 2017 or 2018?
Enter 1 for 2017 or 2 for 2018: 2
**************************************************
The list of friends from 2017:
['Jessica', 'Sarah', 'Ashkan', 'Mina']
--------------------------------------------------
The list of friends from 2018:
['Josh', 'Gurpreet', 'Nyi', 'Carissa', 'Josh', 'Myra', 'Sam']
**************************************************
Done!

'''