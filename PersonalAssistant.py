class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
      self.todos = todos
      self.birthdays = birthdays
      self.contacts = contacts

    def add_todo(self, new_item):
      self.todos.append(new_item)

    def remove_todo(self, todo_item):
      if todo_item in self.todos:
        # Get the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
      else:
        print("Todo is not in list!")

    def get_todos(self):
      return self.todos

    def get_birthdays(self):
      return self.birthdays

    def get_contacts(self):
      return self.contacts

    def get_birthday(self, name):
      if name in self.birthdays:
        return f"{name}'s birthday is on {self.birthdays[name]}."
      else:
        return "Can't find a birthday for this person."

    def add_birthday(self, name, date):
      if name in self.birthdays:
        return f"{name} already exists."
      else:
        self.birthdays[name] = date
        return f"{name} was successfully added!"

    def remove_birthday(self, name):
      if name in self.birthdays:
        self.birthdays.pop(name)
        return f"{name}'s birthday has been removed."
      else:
        return "Sorry, This person does not exist."
  
    def get_contact(self, name):
      if name in self.contacts:
        return f"\nName: {name} \nPosition: {self.contacts[name]}"
      else:
        return "Can't find a contact for this person."

    def add_contact(self, name, job):
      if name in self.contacts:
        return f"{name} already exists."
      else:
        self.contacts[name] = job
        return f"{name} was successfully added!"

    def remove_contact(self, name):
      if name in self.contacts:
        self.contacts.pop(name)
        return f"{name} has been removed."
      else:
        return "Sorry, This person does not exist."



