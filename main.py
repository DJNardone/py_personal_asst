#imports files
import json
from PersonalAssistant import PersonalAssistant

with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)
  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays *****
    4: Get a Birthday
    5: Add a Birthday
    6: Remove a Birthday
    **** Contacts *****
    7: Find a Specific Contact
    8: Add a Contact
    9: Remove a Contact
    
    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # get birthday
    elif user_command == "4":
      print("\nYour Birthdays List: \n")
      for name in assistant.get_birthdays():
        print(name)
      user_input = input("\nWho's Birthday are you looking for today? ")
      print(f"\n {assistant.get_birthday(user_input)}")
    # add birthday
    elif user_command == "5":
      print("\nLet's add a Birthday! \n")
      name = input("Name of the person: ")
      birthday = input("\nTheir birthday (ex: 08/18/2000): ")
      print(f"\n {assistant.add_birthday(name, birthday)}")
    # remove birthday
    elif user_command == "6":
      print("\nYour Birthdays List: \n")
      for name in assistant.get_birthdays():
        print(name)
      user_input = input("\nWho's Birthday would you like to remove? ")
      print(f"\n {assistant.remove_birthday(user_input)}")
    # get contact
    elif user_command == "7":
      print("\nYour Contacts List: \n")
      for name in assistant.get_contacts():
        print(name)
      user_input = input("\nWho are you looking for today? ")
      print(f"\n {assistant.get_contact(user_input)}")
    # add contact
    elif user_command == "8":
      print("\nLet's add a Contact! \n")
      name = input("Name: ")
      position = input("\nPosition: ")
      print(f"\n {assistant.add_contact(name, position)}")
    # remove contact
    elif user_command == "9":
      print("\nYour Contacts List: \n")
      for name in assistant.get_contacts():
        print(name)
      user_input = input("\nWho would you like to remove? ")
      print(f"\n {assistant.remove_contact(user_input)}")
    # exit app
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todos(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)