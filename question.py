# Which of the following is not a mutable data type in Python?
#     answer: C


# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.
even_squares = [i*i for i in range(0, 11) if i % 2 == 0]
print(even_squares)


# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
div_by_2_3 = [i for i in range(0, 11) if i % 2 == 0 and i % 3 == 0]
print(div_by_2_3)

# Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {
        "name": "John",
        "age": 24
    },
    {
        "name": "Anna",
        "age": 22
    },
    {
        "name": "Mike",
        "age": 25
    }
]
for student in student_list:
    print(f"{student['name']} - {student['age']}")


# Write a function combine_words that accepts any number of positional arguments and key-value arguments.
# The function should return a single sentence combining all the words provided.
def combine_words(*args, **kwargs):
    return ' '.join(args + tuple(kwargs.values()))


print(combine_words("Hello", "world", second="is", third="great!", first="Python"))


# Create a class Vehicle with string attributes type, brand, and integer attribute year.
# Ensure instances of the vehicle cannot be created if any of these attributes are missing and
# include a method to display the vehicle’s info. Use dunder method.
class Vehicle:
    def __init__(self, type, brand, year):
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"


# Create a class Car with string attributes brand, model, and integer attribute mileage.
# Implement a method to return the car’s details.
class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage} miles"


# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity.
# Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery
# capacity only if the new value is positive.
class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    def get_details(self):
        car_details = super().get_details()
        return f"{car_details}, Battery Capacity: {self.__battery_capacity}"

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity
        else:
            print("Battery capacity must be a positive value.")


# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder.
# Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and
# a static method for a bank policy message. Ensure the balance is non-negative.
class BankAccount:
    __accounts_created = 0

    @staticmethod
    def bank_policy():
        return "Thank you for choosing our bank. We prioritize your financial security."

    @classmethod
    def accounts_created(cls):
        return cls.__accounts_created

    def __init__(self, account_holder, initial_balance=0.0):
        self._account_holder = account_holder
        # Ensure the balance is non-negative
        self._balance = max(0.0, initial_balance)
        BankAccount.__accounts_created += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def view_balance(self):
        return f"Account Holder: {self._account_holder}, Balance: ${self._balance:.2f}"



# Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
import numpy as np

array = np.arange(1, 10).reshape(3, 3)

print(array)



# Replace non-numeric values in column “A” with the mean of numeric values. Plot a histogram of the “A” column using matplotlib.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})


df['A'] = pd.to_numeric(df['A'], errors='coerce') # Convert column 'A' to numeric 
mean_a = df['A'].mean(skipna=True) # Calculate the mean of column 'A'
df['A'].fillna(mean_a, inplace=True) # Fill NaN values in column 'A' with the calculated mean

plt.hist(df['A'], bins=10, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Column A')
plt.show()




# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.
## continuing from ploting part

# Plot columns 'A' and 'B' using matplotlib
plt.plot(df['A'], label='A')
plt.plot(df['B'], label='B')

# Add x-axis label, y-axis label, and title
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Values of Columns A and B')
plt.legend()

# Show the plot
plt.show()