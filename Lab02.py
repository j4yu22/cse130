# 1. Name:
#      Jay
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program reads user credentials from a JSON file and checks if the user-provided credentials are valid.
# 4. What was the hardest part?
#      The most challenging part was working with JSON's and interpreting them. Since I haven't worked with the json python library I had to figure out syntax
#      and which methods I needed. After a little bit of searching around I was able to get it figured out tho. Testing took a bit
#      too, I don't know who made all of the usernames and passwords more than 10 characters each but geez.
# 5. How long did it take for you to complete the assignment?
#      It took about an hour, I had to test it quite a bit, and I haven't worked with the json library before

import json


def load_creds(filename):
    """
    Opens JSON and parses data.

    Parameters: none
    Returns: two lists containing username and password data from JSON
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data['username'], data['password']
    except FileNotFoundError:
        print(f"Unable to open file {filename}.")
        exit()
        

def check(usernames, passwords):
    """
    Takes the lists, checks if user inputs a good username, checks the appropriate password, and if it matches authenticates.
    Otherwise it doesn't.

    Parameters: 'usernames' and 'passwords' lists
    Returns: none
    """
    username = input("Username: ")
    password = input("Password: ")

    if username in usernames:
        user_index = usernames.index(username)
        if password == passwords[user_index]:
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")
    else:
        print("You are not authorized to use the system.")


def main():
    username, password = load_creds('Lab02.json')
    while True:      # I added this loop so that testing wouldn't take absolutely forever
        check(username, password)

if __name__ == "main":
    main()