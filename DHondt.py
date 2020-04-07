
numberOfParties = input()

###  1. Input number of parties that took part in the election
###  2. Call the input() as many times as you have parties
###  3. Print out the information you have gotten this way.
###  4. (optional) save the vote tally to a file.

 -
print("To add number of seats press 's', to add a party press 'p' to add votes to a party press 'v' ")
print("To see current tally press 't' to run election type 'democracy?'")

def add_party():
    party = input("Enter a name: ")
    votes = input("enter the number of votes: ")

    party.append({
        'party': party,
        'votes': votes,
})

def add_seats

def seats_allocated

def votes_total
#basic d'hondt quotient = votes_total divided by seats_allocated + 1
def quotient

    #this one needs to print the list, wherever that list is
def see_tally():
    print()

user_options = {
    "s": add_seats,
    "p": add_party,
    "v": add_votes,
    "t": see_tally,
    "democracy?": run_demo,
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command, please try again.")

        selection = input(MENU_PROMPT)

menu()