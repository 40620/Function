#Danish Ali
#function development exercise part 1

def user_information():
    hours = int(input("Please enter the number of hours :"))
    minutes = int(input("Please enter the number of minutes :"))
    seconds = int(input("Please enter the number of seconds : "))
    return hours,minutes,seconds

def calculation(hours,minutes,seconds):
    hours = hours * 120
    minutes = minutes * 60
    total = seconds + minutes + hours
    return total

def answer(total):
    print("The total is {0:.2f} seconds".format(total))
           
def main():
    hours,minutes,seconds = user_information()
    total = calculation(hours,minutes,seconds)
    total_answer = answer(total)

#main program
main()
