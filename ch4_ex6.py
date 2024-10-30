# Ch.4, Ex.6
# Saba Feilizadeh
# Validating the user's input (email format) and printing the domain


# Try to get a valid email address from the user with a loop
flag = True

while flag:
    try:
        # Get the user's input
        email = input("Please enter a valid email address: ").strip()

        # The input should not have any spaces
        if " " not in email:
            
            # Check if the input has "@" and "."
            if "@" in email:
                at_position = email.find("@")

                if "." in email:
                    dot_position = email.find(".")

                    # Print the domain name for the user
                    domain = email[at_position + 1 : dot_position]
                    print(domain)
                    
                    flag = False
            
        else:
            print("The input should not have any spaces. Please try again!")

    except:
        print("Error, please enter a valid email address!")
        print("******************************************")

print("Done!")    



'''
Outputs:

Please enter a valid email address: joe@yahoo.com 
yahoo
Done!

---------------------------------------------------

Please enter a valid email address: hello.com
Please enter a valid email address: hello@gmail
Please enter a valid email address: hello  @world.com
The input should not have any spaces. Please try again!
Please enter a valid email address: hello@world.com
world
Done!

'''
