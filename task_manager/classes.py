"""
Classes
"""

class Task():
    def __init__(self, name, description, date, is_completed):
        self.name = name
        self.description = description
        self.date = date
        self.is_completed = is_completed
    def __str__(self):
        return f"{self.name}\nDate: {self.date}\nCompleted?: {self.is_completed}"

class Menu():
    def __init__(self, is_at_menu, choice):
        self.is_at_menu = is_at_menu
        self.choice = choice


"""
Functions
"""
