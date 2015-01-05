
#Danish Ali
#Function class exercisepart 4


def input_information():
    Fahrenheit = float(input("please enter the temperature in Fahrenheit: "))
    return Fahrenheit

def calculate(Fahrenheit):
    Celsius = (Fahrenheit-32)*(5/9)
    return Celsius

def display(Celsius):
    print("Temperature in Celsius is {0:.2F}".format(Celsius))

def main():
    print("This program will convert temperature from Fahrenheit into Celsius")
    print()
    Fahrenheit = input_information()
    Celsius = calculate(Fahrenheit)
    display(Celsius)
