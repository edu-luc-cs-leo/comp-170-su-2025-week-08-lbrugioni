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
        """Returns the person's birthday in a readable style like 23rd of April.
           If their is no birthday given it returns Birthday is not given """
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

            months= ['January','February','March','April','May','June','July','August','September','October','November','December']
            month= months[month_number-1] #Convert month number to months name 
            result=f"{day}{ending} of {month}"
        #If data is not given, avoid error by printing "Birthday is not given'"
        else:
            result="Birthday is not given"

        return result
    
    def __lt__(self,other): # Create a special method and call < between two objects
        """Return True if self's first name is alphabetcially less than the other's first name.""" 
        return self.first_name < other.first_name 

#Test Code
print ()

#Test Code for say_birthday
p1=Person("Lillie","Brugioni") #testing no birthday 
print(p1.say_birthday())

p2=Person("Sara","Odish") #testing "th" ending 
p2.birthday=Birthday(8,4)
print(p2.say_birthday())

p3=Person("Lillie","Brugioni") #testing "rd" ending 
p3.birthday=Birthday(4,23)
print(p3.say_birthday())

p4=Person("Claire", "Brugioni") #testing "st" ending 
p4.birthday=Birthday(1,1)
print(p4.say_birthday())

p5=Person("Michelle", "Smith") #testing invalid birthday 
p5.birthday=Birthday(2,30)
print(p5.say_birthday())

print()

#Test self name
p1=Person("Sara","Bob")
p2=Person("Lillie","Brugioni")

print(p1 < p2)
print(p1 > p2)

print ()







