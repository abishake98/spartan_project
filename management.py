import spartan
import json

def read_main_option():
    print("What would you like to do? ")
    print("-----------------------------------------")

    print("1) Add a Spartan")
    print("-----------------------------------------")
    print("2) Remove a Spartan")
    print("-----------------------------------------")
    print("3) Get Total Number of Spartans")
    print("-----------------------------------------")
    print("4) Get List of All Spartans")
    print("-----------------------------------------")
    print("5) Retrieve the Data of a Spartan (by Spartan ID)")
    print("-----------------------------------------")
    print("6) Save as JSON File")
    print("-----------------------------------------")
    print("7) Load JSON File")
    print("-----------------------------------------")
    print("8) Exit")
    print("-----------------------------------------")

    choice = input("Please Select One of the Above Options (1/2/3/4/5/6/7/8): ")
    choice = choice.strip()
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return choice
    else:
        print("Warning: Invalid Option! Please Try Again")

def read_update_option():
    print("What Would You Like to Update For This Spartan?")
    print("1) Spartan First Name")
    print("2) Spartan Last Name")
    print("3) Birth Day")
    print("4) Birth Month")
    print("5) Birth Year")
    print("6) Course")
    print("7) Stream")
    print("8) Back to Menu")

    choice = input("Please Select One of the Above Options (1/2/3/4/5/6/7/8): ")
    choice = choice.strip()
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return
    else:
        print("Warning: Invalid Option! Please Try Again")

def save_to_json():
    temp_dict_of_dict = {}
    for spartan_id in all_spartan_dictionary:
        spartan_obj = all_spartan_dictionary[spartan_id]
        spartan_dict = spartan_obj.__dict__
        temp_dict_of_dict[spartan_id] = spartan_dict

    with open("spartan.json", "w") as spartan_file:
        json.dump(temp_dict_of_dict, spartan_file, indent= 8)

def load_from_json():
    global all_spartan_dictionary
    temp_dict_of_dict = {}
    try:
        with open("spartan.json", "r") as spartan_file:
            temp_dict_of_dict = json.load(spartan_file)
    except:
        print("The file spartan.json doesn't exist")

    print(temp_dict_of_dict)

    for spartan_id_key in temp_dict_of_dict:
        spartan_id = temp_dict_of_dict[spartan_id_key]["spartan_id"]
        first_name = temp_dict_of_dict[spartan_id_key]["first_name"]
        last_name = temp_dict_of_dict[spartan_id_key]["last_name"]
        birth_day = temp_dict_of_dict[spartan_id_key]["birth_day"]
        birth_month = temp_dict_of_dict[spartan_id_key]["birth_month"]
        birth_year = temp_dict_of_dict[spartan_id_key]["birth_year"]
        course = temp_dict_of_dict[spartan_id_key]["course"]
        stream = temp_dict_of_dict[spartan_id_key]["stream"]

        spartan_obj = spartan.Spartan(spartan_id, first_name, last_name, birth_day, birth_month, birth_year, course, stream)

        all_spartan_dictionary[spartan_id] = spartan_obj

if __name__ == "__main__":

    print("---------------------------------------------------------")
    print("WELCOME TO THE SPARTA GLOBAL'S EMPLOYEE MANAGEMENT SYSTEM")
    print("---------------------------------------------------------")

    all_spartan_dictionary = {}
    load_from_json()

    while True:

        main_menu_option = read_main_option()

        if main_menu_option == "1":

            while True:
                spartan_id = spartan.read_spartan_id()
                if spartan_id in all_spartan_dictionary.keys():
                    print("WARNING: Spartan ID Already Exists")
                else:
                    break
            first_name = spartan.read_first_name()
            last_name = spartan.read_last_name()
            birth_day = spartan.read_birth_day()
            birth_month = spartan.read_birth_month()
            birth_year = spartan.read_birth_year()
            course = spartan.read_course()
            stream = spartan.read_stream()

            spartan_object = spartan.Spartan(spartan_id, first_name, last_name, birth_day, birth_month, birth_year, course, stream)

            all_spartan_dictionary[spartan_id] = spartan_object

            save_to_json()

            print(all_spartan_dictionary)

        elif main_menu_option == "2":
            if len(all_spartan_dictionary) == 0:
                print("Unable to Remove Employee")

            else:
                while True:
                    spartan_id_remove = spartan.read_remove_spartan_id()
                    if spartan_id_remove in all_spartan_dictionary.keys():
                        break
                    else:
                        print("WARNING: Spartan ID entered doesn't exist in the system")

                del all_spartan_dictionary[spartan_id_remove]

                save_to_json()

        elif main_menu_option == "3":
            print(f"The Total Number of Spartans Working at Sparta Global is {len(all_spartan_dictionary)}")

        elif main_menu_option == "4":
            for spartan_id in all_spartan_dictionary:
                print(f"The details of the Spartan, with Spartan ID {spartan_id}, can be found below:")
                all_spartan_dictionary[spartan_id].print_spartan_data()

        elif main_menu_option == "5":
            while True:
                spartan_id_view = spartan.read_view_spartan_id()
                if spartan_id_view in all_spartan_dictionary.keys():
                    print(f"The details of the Spartan, with Spartan ID {spartan_id_view}, can be found below:")
                    all_spartan_dictionary[spartan_id_view].print_spartan_data()
                    break
                else:
                    print("WARNING: Spartan ID entered doesn't exist in the system")

        elif main_menu_option == "6":
            save_to_json()

        elif main_menu_option == "7":
            load_from_json()

        elif main_menu_option == "8":
            break

        else:
            print("Invalid Option! Please Try Again")


