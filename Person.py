from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"

    def say_birthday(self):
        #Check if birthday was given 
        if self.birthday is not None:
            day=self.birthday.get_day()
            month_number=self.birthday.get_month()
        #Choose the right ending letters for the specfic number date 
            if day in [1,21,31]:
                ending='st'
            elif day in [2,22]: #Use elif statments to avoid using mutiple if statments 
                ending='nd'
            elif day in [3,23]:
                ending="rd"
            else:
                ending="th"

            month= ['January','February','March','April','May','June','July','August','September','October','November','December']

            result=f"{day}{ending} of {month[month_number-1]}"
        #If data is not given, avoid error by printing "Birthday is not given'"
        else:
            result="Birthday is not given"

        return result
    
#__It__ stands for less than ans is called when you use < inbetween two objects
def __It__(self,other): # Create a special method and call < between two objects
    return self.first_name < other.first_name 
