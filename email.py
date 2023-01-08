# Create class "Email".
class Email:

    # Define __init__() to assign values for "email_contents" and from_address",
    # also initialise "is_spam" and "has_been_read" to False.
    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

    # Define "mark_as_read(self)" to mark email as read, switch "has_been_read" from False to True.
    def mark_as_read(self):
        self.has_been_read = True

    # Define "mark_as_spam(self)" to mark email as spam , switch "is_spam" from False to True.
    def mark_as_spam(self):
        self.is_spam = True

    # Define __Str__ (self) to print self.email_contents and self.from_address.
    def __str__(self):
        return f"{self.email_contents}, {self.from_address}"

    def __repr__(self):
        return f'{self.email_contents} {self.from_address}'

# Create an empty list for email inbox and store in "inbox".
inbox = []


# Define function "add_email" with parameters of contents and email_address to add email with message.
# Variable "email" store the class Email(contents, email_address), then append "email" to the "inbox" list.
def add_email(contents, email_address):
    email = Email(contents, email_address)
    inbox.append(email)


# Define function "get_count()" to provides the count of emails within inbox and return the length of "inbox" list.
def get_count():
    return len(inbox)


# Define function "get_email" with parameter (i) to provides the email present the specified index.
def get_email(i):
    # If "index" is larger or equal to 0 and smaller than the length of inbox,
    # "email" stores at position i in the list,
    # the email will be mark as read by using defined mark_as_read() and print "email"
    # Returns the contents of an email in the list
    if 0 <= i < len(inbox):
        email = inbox[i]
        email.mark_as_read()
        print(f"{email}\n")
        return email

    # Else, if it is out of range, print error message.
    else:
        print('Invalid index, email does not exist')


# Define function "get_unread_emails" to provides all unread emails.
# Create an empty list and store in "unread_list".
def get_unread_emails():
    unread_list = []

    # For "emails" in inbox,
    # if emails.has_been_read is False, append emails to unread_list,
    # return "unread_list" - a list of all the emails that have not been read.
    for emails in inbox:
        if not emails.has_been_read:
            unread_list.append(emails)
    return unread_list


# Define function get_spam_emails() to provides all spam mails and create an empty list called "spam_list".
def get_spam_emails():
    spam_list = []

    # For "emails" in inbox, if emails.is_spam is False, append "emails" to spam_list and print the spam email contents.
    # Return "spam_list".
    for emails in inbox:
        if emails.is_spam:
            spam_list.append(emails)
            inbox.remove(emails)
            print(f"Spam message: {emails.email_contents}\n")
    return spam_list


# Define function "add_spam" with "index" as parameter to add the specified index email as spam.
# "message" is equal to inbox[index] and "message" will be marked as spam using defined "mark_as_spam()" function.
# Print message "Email added to spam."
def add_spam(index):
    messages = inbox[index]
    messages.mark_as_spam()
    print("Email added to spam.")


# Define function "delete" with parameter "index" to delete the email from inbox.
# If the length of inbox is more than 0, return inbox.pop(index) the remove the email.
# Else, print message "Email cannot be deleted".
def delete(index):
    if len(inbox) > 0:
        print("Email has been deleted")
        inbox.pop(index)

        return
    else:
        print("Email cannot be deleted.")


# Prepopulated emails with messages and store in "emails_list".
emails_list = ["Nice to meet you, john_wick@gmail.com",
               "Please attend the meeting on Monday, boss@icloud.com",
               "Deadline has been postponed to 5th Jan, lecturer@oxford.ac.uk",
               "Congratulation! You have passed your theory test, dvla@gov.co.uk",
               "Thank you for your Steam purchase!, noreply@steampowered.com"]

# Use for loop to loop through the "email_list", for emails in email_list.
# Variables "message" and "email" is equal to split(",") of the items in the list and use add_email function.
for emails in emails_list:
    message, email = emails.split(',')
    add_email(message, email)

# Create an empty string and store in "user_choice".
user_choice = ""

# Use while loop to verify user's choice. While user's input is not "6",
# Create a menu and request user's input of their choice and store in "user_choice".
while user_choice != "6":
    user_choice = input("Select an option.\n1. Read emails\n2. Mark spam\n3. Send email\n4. Delete email\n"
                        "5. Total numbers of email\n6. Exit\nEnter a number to proceed: ")

    # If "user_choice" is "1", initialize to read email.
    # In another while loop, for "email_num" and "email_address" in enumerate(emails_list), then print list of emails.
    if user_choice == "1":
        while True:
            print("\nList of unread email:\n")
            for email_num, email_address in enumerate(emails_list):
                print(f'{email_num + 1}. {email_address}')

            # Under try block, ask user's choice of which email to read and
            # use get_email() to display the email, then break.
            # Except IndexError and ValueError if user's input is invalid and print the appropriate message.
            try:
                email_choice = int(input("\nEnter number of email you want to read: "))
                get_email(email_choice - 1)
                print(emails_list)
                break
            except IndexError:
                print("Email does not exist.\n")
            except ValueError:
                print("Invalid input.\n")

    # Elif, if user's input is "2", initialize spam email_address marking option.
    # In another while loop, for "email_num" and "email_address" in enumerate(emails_list), then print list of emails.
    elif user_choice == "2":
        while True:
            print("\nList of emails\n")
            for email_num, email_address in enumerate(emails_list):
                print(f"{email_num + 1}. {email_address}")

            # Under try block, ask for email choice from user to mark spam,
            # Use add_spam function and print the spam message using get_spam_emails() function and break.
            # Except IndexError and ValueError if user's input is invalid and print the appropriate message.
            try:
                email_choice = int(input("\nEnter number of email you want to spam: "))
                add_spam(email_choice - 1)
                get_spam_emails()
                print(inbox)
                break
            except IndexError:
                print("Email does not exist.")
            except ValueError:
                print("Invalid input.")

    # Elif, user's choice is "3", initialize to send email.
    # Ask user to input an email and email contents, then store in variable "from_address" and "email_contents".
    # Call the add_email function with parameters email_contents and from_address, then print successful message.
    elif user_choice == "3":
        from_address = input("Enter an email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address)
        print("Email sent successfully!\n")

    # Elif, user's choice is 4, initialize to delete email.
    # In another while loop, for "email_num" and "email_address" in enumerate(emails_list), then print list of emails.
    elif user_choice == "4":
        while True:
            print("\nList of emails\n")
            for email_num, email_address in enumerate(emails_list):
                print(f"{email_num + 1}. {email_address}")

            # Under try block, ask for email choice from user to delete.
            # Use the get_email function to display the selected email and delete() to delete the email and break.
            # Except IndexError and ValueError if user's input is invalid and print the appropriate message.
            try:
                email_choice = int(input("\nEnter number of email you want to delete: "))
                get_email(email_choice - 1)
                delete(email_choice - 1)
                print(inbox)
                break
            except IndexError:
                print("Email does not exist.")
            except ValueError:
                print("Invalid input.")

    # Elif "user_choice" is "5", print the total number of emails by calling get_count() function.
    elif user_choice == "5":
        print(f"There are {get_count()} emails in the inbox.\n")

    # Elif, user's input is "4", print goodbye message and use exit() to leave the menu.
    elif user_choice == "6":
        print("Goodbye!")
        exit()

    # Otherwise, print error message.
    else:
        print("Oops - incorrect input!\n")
