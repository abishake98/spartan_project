
class Spartan:

    def __init__(self, spartan_id, first_name, last_name, birth_day, birth_month, birth_year, course, stream):
        self.set_spartan_id(spartan_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_birth_day(birth_day)
        self.set_birth_month(birth_month)
        self.set_birth_year(birth_year)
        self.set_course(course)
        self.set_stream(stream)

    def get_spartan_id(self):
        return self.spartan_id

    def set_spartan_id(self, new_spartan_id):
        if new_spartan_id > 0:
            self.spartan_id = new_spartan_id
            print(f"Spartan's ID is {self.spartan_id}")
        else:
            return print("The Spartan ID is Invalid")

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        if len(new_first_name.strip()) >= 2:
            self.first_name = new_first_name
            print(f"Spartan's First Name is {self.first_name}")
        else:
            return print("Spartan's First Name is Invalid")

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        if len(new_last_name.strip()) >= 2:
            self.last_name = new_last_name
            print(f"Spartan's Last Name is {self.last_name}")
        else:
            return print("Spartan's Last Name is Invalid")

    def get_birth_day(self):
        return self.birth_day

    def set_birth_day(self, new_birth_day):
        if 1 <= new_birth_day <= 31:
            self.birth_day = new_birth_day
            print(f"Spartan's Day of Birth is {self.birth_day}")
        else:
            return print("Spartan's Day of Birth is Invalid")

    def get_birth_month(self):
        return self.birth_month

    def set_birth_month(self, new_birth_month):
        if 1 <= new_birth_month <= 12:
            self.birth_month = new_birth_month
            print(f"Spartan's Month of Birth is {self.birth_month}")
        else:
            return print("Spartan's Month of Birth is Invalid")

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, new_birth_year):
        if 1900 <= new_birth_year <= 2004:
            self.birth_year = new_birth_year
            print(f"Spartan's Month of Year is {self.birth_year}")
        else:
            return print("Spartan's Year of Birth is Invalid")

    def get_course(self):
        return self.course

    def set_course(self, new_course):
        if len(new_course.strip()) > 0:
            self.course = new_course
            print(f"Spartan's Course is {self.course}")

        else:
            return print("Spartan's Course is Invalid")

    def get_stream(self):
        return self.stream

    def set_stream(self, new_stream):
        if len(new_stream.strip()) > 0:
            self.stream = new_stream
            print(f"Spartan's Stream is {self.stream}")
        else:
            return print("Spartan's Stream is Invalid")

    def print_spartan_data(self):
        spartan = {"Spartan ID" : self.spartan_id,
                   "Spartan's First Name" : self.first_name,
                   "Spartan's Last Name" : self.last_name,
                   "Spartan's Day of Birth" : self.birth_day,
                   "Spartan's Month of Birth" : self.birth_month,
                   "Spartan's Year of Birth" : self.birth_year,
                   "Spartan's Course" : self.course,
                   "Spartan's Stream" : self.stream}

        return print(spartan)

    def __str__(self):
        return f"Spartan ID: {self.spartan_id} --- Spartan's First Name: {self.first_name} --- Spartan's Last Name: {self.last_name} --- Spartan's Day of Birth: {self.birth_day} --- Spartan's Month of Birth: {self.birth_month} --- Spartan's Year of Birth: {self.birth_year} --- Spartan's Course: {self.course} --- Spartan's Stream: {self.stream}"

def read_spartan_id():
    while True:
        spartan_id_str = input("Please Enter Your Spartan ID: ")
        if spartan_id_str.isdigit():
            spartan_id = int(spartan_id_str)
            return spartan_id

        else:
            print("WARNING: Please Enter a Valid Spartan ID")

#First Name
def read_first_name():
    while True:
        first_name = input("Please Enter Your First Name: ")

        if len(first_name.strip()) >= 2:
            return first_name

        else:
            print("WARNING: Your First Name Should Be At Least 2 Characters")

#Last Name
def read_last_name():
    while True:
        last_name = input("Please Enter Your Last Name: ")

        if len(last_name.strip()) >= 2:
            return last_name

        else:
            print("WARNING: Your Last Name Should Be At Least 2 Characters")

#Birthyear
def read_birth_year():
    while True:
        birth_year_str = input("Please Enter Your Year of Birth: ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                return birth_year
            else:
                print("WARNING: Please Enter a Valid Year of Birth")

        else:
            print("WARNING: Please Enter a Valid Year of Birth")

#Birthmonth
def read_birth_month():
    while True:
        birth_month_str = input("Please Enter Your Month of Birth, as a Number: ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            else:
                print("WARNING: Please Enter a Valid Month of Birth")

        else:
            print("WARNING: Please Enter a Valid Month of Birth")

#Birthday
def read_birth_day():
    while True:
        birth_day_str = input("Please Enter Your Day of Birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                return birth_day
            else:
                print("WARNING: Please Enter a Valid Day of Birth")

        else:
            print("WARNING: Please Enter a Valid Day of Birth")

def read_course():
    while True:
        course = input("Please Enter Your Course: ")
        if len(course.strip()) > 0:
            return course
        else:
            print("WARNING: Please Enter a Valid Course")

def read_stream():
    while True:
        stream = input("Please Enter Your Stream: ")
        if len(stream.strip()) > 0:
            return stream
        else:
            print("WARNING: Please Enter a Valid Stream")

def read_remove_spartan_id():
    while True:
        remove_id_str = input("Which Spartan ID Would You Like to Remove From the System? ")
        if remove_id_str.isdigit():
            remove_id = int(remove_id_str)
            return remove_id
        else:
            print("WARNING: Enter a Valid Spartan ID")

def read_view_spartan_id():
    while True:
        view_id_str = input("Which Spartan ID Would You Like to View From the System? ")
        if view_id_str.isdigit():
            view_id = int(view_id_str)
            return view_id
        else:
            print("WARNING: Enter a Valid Spartan ID")

def read_update_employee_id():
    while True:
        update_id_str = input("Which Spartan ID Would You Like to Update From the System? ")
        if update_id_str.isdigit():
            update_id = int(update_id_str)
            return update_id
        else:
            print("WARNING: Enter a Valid Spartan ID")
