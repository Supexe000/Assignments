# Assignment No 1
# Week 1

print("Welcome to the Python Assignment!")

# Question 1: Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Question 2: Calculate Area of a Rectangle
length = 10
width = 5
area = length * width
print(f"Area of Rectangle = {area}")

# Question 3: Calculate Compound Interest
P = 10000  # Principal
R = 5      # Rate
T = 2      # Time
CI = P * (1 + R/100)**T - P
print(f"Compound Interest = {CI}")

# Question 4: Perimeter of a Rectangle
length = 12
width = 8
perimeter = 2 * (length + width)
print(f"Perimeter of Rectangle = {perimeter}")

# Question 5: Average of Three Numbers
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print(f"Average = {average}")

# Question 6: Square and Cube of a Number
num = 4
square = num ** 2
cube = num ** 3
print(f"Square = {square}, Cube = {cube}")

# Question 7: Distribute Items Equally
candies = 50
students = 6
each_gets = candies // students
left = candies % students
print(f"Each student gets {each_gets} candies")
print(f"Candies left: {left}")

# Question 8: Profit or Loss
cost_price = 150
selling_price = 180
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit = {profit}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss = {loss}")
else:
    print("No Profit No Loss")

# Question 9: Total Marks, Percentage, Average
marks = [85, 90, 78, 92, 88]
total = sum(marks)
percentage = (total / 500) * 100
average = total / len(marks)
print(f"Total = {total}, Percentage = {percentage}%, Average = {average}")

# Question 10: Salary Calculator
basic_salary = 30000
hra = 0.20 * basic_salary
da = 0.15 * basic_salary
total_salary = basic_salary + hra + da
print(f"Total Salary = {total_salary}")

# Question 11: Age in Months and Days
age_years = 20
months = age_years * 12
days = age_years * 365  # Approximate
print(f"Age = {months} months or {days} days")

# Question 12: USD to PKR Conversion
usd = 100
exchange_rate = 280  # Fixed
pkr = usd * exchange_rate
print(f"${usd} = Rs.{pkr}")

# Question 13: Sum of First N Natural Numbers
n = 10
sum_n = n * (n + 1) // 2
print(f"Sum of first {n} natural numbers = {sum_n}")

# Question 14: Percentage of Correct Answers
total_questions = 40
correct_answers = 32
percentage = (correct_answers / total_questions) * 100
print(f"Score = {percentage}%")

# Question 15: Speed, Distance, Time
distance = 150  # km
time = 2        # hours
speed = distance / time
print(f"Speed = {speed} km/h")

# Question 16: Body Mass Index (BMI)
weight = 70     # kg
height = 1.75   # meters
bmi = weight / (height ** 2)
print(f"BMI = {bmi}")

# Question 17: Convert Minutes to Hours and Minutes
minutes = 130
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")

print("All assignments completed successfully!")



