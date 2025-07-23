from datetime import datetime

class Birthday:

    # Some data for this object: the number of days in each month.
    # For simplicity, we ignore leap years and keep February at 28.
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        """Basic constructor. It validates the arguments past to it
        and if they are out of range, it assigns a default value of
        January 1."""
        # Protect month value
        if month >= 1 and month <= 12:
            self.__month = month
        else:
            # In case of out of range month, default to January
            self.__month = 1
        # At this point we have a legit month value 1-12.
        # Protect day value; use -1 in array to synchronize months
        if day >= 1 and day <= Birthday.days_in_month[month - 1]:
            self.__day = day
        else:
            # In case of out of range day, default is 1st of month
            self.__day = 1
    # end basic constructor

    def set_day(self, day):
        """Mutator for day. It only changes the day value if the
        passed argument is within a valid range for the given month."""
        if day > 0 and day <= Birthday.days_in_month[self.__month-1]:
            self.__day = day
    # end set_day

    # Accessor for __month
    def get_month(self):
        return self.__month

    # Accessor for __day
    def get_day(self):
        return self.__day
    
    
    def days_until(self):
       """Calculate the number of days from today until the next birthday. Assumes all years are 365 days. """
       today=datetime.today() #obtain today's date 
       today_day=self.day_in_year(today.month,today.day) # extract month and day
       bday_day=self.day_in_year(self.__month,self.__day) #subtract from birthday

       if bday_day>today_day: #Birthday is coming up later in the year 
           result= bday_day-today_day 
       else: 
        result=365+(bday_day-today_day) #Birthday has already passed 
        return result 
       
        
    def day_in_year(self, month, day):
        """calculates the day number within the year corresponding to a given 
        date (month, day), assuming that February has 28 days always."""
        count = 0
        for i in range(month-1):
            count += Birthday.days_in_month[i]
        return count + day

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.get_month()}/{self.get_day()} ]"

    def set_month(self,month):
        """Set the month if valid (1-12). Reset day to 1 if inputed 
         day is invalid for the specified month."""
        #Check if the month number is valid
        if 1<=month <=12:
            #Check if the current day is incorrect for the given month
            if self.__day> Birthday.days_in_month[month-1]:
                self.__day=1
            self.__month=month
        
#Test Code

demo = Birthday(6,29)

print(demo.day_in_year(6,29)) # d_b
print(demo.day_in_year(4,29)) # d_t

print()

#Test for set_month ()
bday=Birthday(4,30)
print(bday)
bday.set_month(2) #sets day back to 1 for invalid dyas in month 
print(bday)

print()

#Test days_until()
bday=Birthday(4,23)
print(bday.days_until())
