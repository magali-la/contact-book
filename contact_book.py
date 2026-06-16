# contact book script with multiple options to edit or view it

# contacts dictionary with some starter contacts
contacts = {
    "Bob": ["1234", "2983"],
    "Belle": ["1092"],
    "Olivia": ["2983", "2904", "9390"]
}

# helper functions for different actions
# add contact - they add name and number in input / ask if they have more numbers for the person, if yes run the input again, append those to th 
def add_contact():
    print("You're adding a contact")
    # contact array for later
    contact_arr = []
    # flag for if they are done or not
    is_done_adding = False

    contact_name = input("Write a name: ")

    # if the contact is in the dict, then stop this function, they'll have to go back to the menu
    if contact_name in contacts:
        print("This name is already in your contacts. No duplicates.")
        # return cuts this function
        return

    # otherwise run this loop to add numbers
    while is_done_adding == False:
        contact_number = input("Add a number: ")

        # append it to the contact_arr
        contact_arr.append(contact_number)

        more_contacts = input("Do you have more contacts for this person? (Y/N): ")

        # if they don't have more contact, add to dict, update loop flag, then exit this loop
        if (more_contacts == "N"):
            # set the flag to stop this loop
            is_done_adding = True

            # add it to the dictionary
            contacts[contact_name] = contact_arr

            # success message
            print(f"Contact added for {contact_name}.")

            # go back to the menu and break this loop
            break

# view contacts - just print the dictionary
def view_contacts():
    if len(contacts) == 0:
        print("No contacts.")
        # end with return so it goes back to the menu loop
        return
    else:
        print(contacts)

# the while loop needs to keep going until the user picks 5, so the condition can just be true - menu should open up always after a helper is finished
while True:
    try:
        # script opens with the menu
        menu_choice = input("Contact Book Menu:\n 1. Add New Contact \n 2. View All Contacts \n 3. Search Contact \n 4. Delete Contact \n 5. Exit \n Enter your choice (1-5): ")

        menu_num = int(menu_choice)

        # restart if it is a number but not 1-5
        if menu_num < 1 or menu_num > 5:
            print(f"{menu_choice} is not a valid number 1-5. Try again.")
            continue
    except:
        # continue to run the loop again and the menu
        print(f"{menu_choice} isn't a valid number 1-5. Try again")
        continue

    # for the code to get here it should have alredy been 1-5, so the else can just be the 5
    if menu_num == 1:
        add_contact()
    elif menu_num == 2:
        view_contacts()
    # elif menu_num == 3:
    #     search_contact()
    # elif menu_num == 4:
    #     delete_contact()
    else:
        print("Exiting contact book.")
        break