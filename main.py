import os

# collecting user data
def user_data():
    name = input("Enter your name: ")
    city = input("Enter your age: ")
    salary = int(input("Enter your salary: "))
    department = input("Enter your department: ")

    my_dict = {
        'name': name,
        'city': city,
        'salary': salary,
        'dep': department
    }

    return my_dict

# listing all files
def listing_files():

    my_dict = {}    

    for i in os.listdir():
        file_counter = 1
        if i.endswith('.txt'):
            print(f'{filecounter}. {i}')
            file_counter += 1

            

    
    choice = int(input("Enter the number of file which you want to edit : "))
    add_data(choice)
    


# creating file and storing data
def create_a_file():
    file_name = input("Enter the name of the file : ")
    with open(file_name + ".csv", "w+") as file:
        file.writelines("Name, City, Salary, Department")

    print(f"File is created by name {file_name}.csv.")


def add_data(file_number):
    number_of_data = int(input("How many user data you want to add : "))
    


# infinite loop for running program
while True:
    print("WELCOME TO HULULULU")
    choice = int(
        input(
            "1. for listing all files.\n2. for creating a new file.\n3. for adding data in existing file.\n4. for exit from this program"
        )
    )
    if choice == 1:
        pass

    elif choice == 2:
        create_a_file()

    elif choice == 3:
        pass

    elif choice == 4:
        break

    else:
        print("You made a wrong choice.\nPlease try again.")
