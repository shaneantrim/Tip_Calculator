# Welcome to my tip calculator program.

print("Welcome to the tip calculator.")
bill = input("How much is the bill?")
number_of_people = input("How many people are paying?")
tip_percentage = input("What percentage tip would you like to leave?")

bill_as_float = float(bill)
number_of_people_as_int = int(number_of_people)
tip_percentage_as_int = int(tip_percentage)

tip_as_float = tip_percentage_as_int / 100
what_tip_equals = bill_as_float * tip_as_float
total_bill = bill_as_float + what_tip_equals
each_person_pays = total_bill / number_of_people_as_int

print(f"Each person should tip: ${what_tip_equals}")
print(f"Each person should pay: ${each_person_pays:.2f}")
