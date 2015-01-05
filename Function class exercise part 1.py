#output symbol

def name():
        symbol = input("Please enter a sysmbol: ")
        repeat = int(input("Please enter a digit: "))
        return symbol, repeat

def display(symbol,repeat):
            total = repeat * symbol
            return total

def answer(total):
        print = ("your answer is .{0}".format(total))
                                    
def main():
        symbol,repeat = name()
        total = display(symbol,repeat)
        total_answer = answer(total)
        

#main program
main()

    
        
            
    
