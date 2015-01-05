#Danish ALi
#Function class exercise part 3



def user_information():
    number_1 = int(input("Please enter the first number:"))
    number_2 =int(input("Please enter the second number:"))
    return number_1,number_2
    
def display(number_1,number_2):
    if number_1 > number_2:
        print("{1}.{2}".format(number_1,number_2))
    elif number_2 > number_1:
         print("{1}.{2}".format(number_2,number_1))
    
def main():
    name = user_information()
    numbers = display(number_1,number_2)

#main program
main()


    
    
    
    
    
    
    
    
    

