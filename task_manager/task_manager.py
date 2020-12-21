from classes import *


tasks = []
task_001 = Task("Do Laundry", "Go and do the laundry", "31 December", False)
tasks.append(task_001)

#Brings user to main menu
main_menu = Menu(True, None)
view_menu = Menu(False, None)

def goto_menu(input):
    view_menu.choice = None
    main_menu.choice = None
    if input == 'main':
        view_menu.is_at_menu = False
        main_menu.is_at_menu = True

    elif input == 'view':
        main_menu.is_at_menu = False
        view_menu.is_at_menu = True



"""
Main Menu
"""
while main_menu.is_at_menu == True:
    print("---Main Menu---")
    print("What would you like to do?")
    print("View tasks | Create New Task")
    main_menu.choice = input("Please enter V or C then press enter: \n")
    if main_menu.choice == 'V' or main_menu.choice == 'v':
        print("---View Tasks Menu---")
        goto_menu('view')

    elif main_menu.choice == 'C' or main_menu.choice == 'c':
        print("//UNDER CONSTRUCTION")
        goto_menu('main') #BE SURE TO UPDATE TO CREATE

    else:
        print("You did not enter a valid character!")
        goto_menu('main')

"""
View Menu
"""
while view_menu.is_at_menu == True:
        for task in tasks:
            print(f"Task:\n {task}")
        else:
            view_menu.choice = input("What would you like to do? M for main menu: \n")
            if view_menu.choice == 'M' or view_menu.choice == 'm':
                goto_menu('main')
                break







input("<<End of Programme>>")
