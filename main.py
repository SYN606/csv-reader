import os


# collecting user data
def user_data():
    name = input("Enter your name: ")
    city = input("Enter your age: ")
    salary = int(input("Enter your salary: "))
    department = input("Enter your department: ")
    my_dict = {"name": name, "city": city, "salary": salary, "dep": department}

    return my_dict


# listing all files
def listing_files():
    my_dict = {}
    file_counter = 1
    for i in os.listdir():
        if i.endswith(".csv"):
            my_dict.update(
                {file_counter: i},
            )
            file_counter += 1
    return my_dict


# creating file and storing data
def create_a_file():
    file_name = input("Enter the name of the file:\n>>> ")
    file_name = file_name + ".csv"
    # Check if the file already exists
    if os.path.exists(file_name):
        print("\nFile already exists. Please try another name.")

    else:
        with open(file_name + ".csv", "w+") as file:
            file.writelines("Name, City, Salary, Department\n")
        print(f"\nFile is created by name {file_name}.csv.\n")


def add_data():
    all_files = listing_files()
    if all_files:
        for key in all_files.keys():
            print(f"{key}. {all_files[key]}")

        file_sr = int(input("Enter the serial no. of that file you want to edit.\n>>>"))
        file_name = str(all_files[file_sr])
        with open(file_name, "a") as f:
            user_data_no = int(input("\nHow many users data you want to add.\n>>>"))

            for i in range(user_data_no):
                data = user_data()
                for j in data.keys():
                    f.writelines(f"{str(data[j])},")
                f.writelines("\n")

        print("\nALl data is written into csv file successfully.")

    else:
        print("\nNo such files found.Before adding data create a file.\n")


# welcome line
print("\n\n___________WELCOME___________\n\n")


# infinite loop for running program
while True:
    choice = int(
        input(
            "\n1. for listing all files.\n2. for creating a new file.\n3. for adding data in existing file.\n4. for exit from this program\n>>>"
        )
    )
    if choice == 1:
        files = listing_files()
        if files:
            for key in files.keys():
                print(f"{key}. {files[key]}")
        else:
            print("\nNo files found.\n")

    elif choice == 2:
        create_a_file()

    elif choice == 3:
        add_data()

    elif choice == 4:
        print("\nProgram exited successfully.")
        break

    else:
        print("\nYou made a wrong choice.Please try again.\n")
