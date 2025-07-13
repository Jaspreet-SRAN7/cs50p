#cs50p pset0 problem5 (week0) introduction to programming using python.
def main ():
    dollars=dollars_to_float (input("how much was the meal? "))
    percent = percent_to_float(input("what percent would you like to tip? "))
    tip = percent*dollars
    print(f"leave {tip:.2f}")

def dollars_to_float(d):
    dollars=float(dollars.replace("$"," "))

def percent_to_float():
    percent=float(percent.replace("%"," "))

