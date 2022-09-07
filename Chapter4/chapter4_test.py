def loop1(): #example of a while loop
    #1oop1 accepts no arguments
    #loops through 10 times calculating a running total
    #outputs the total as it processes is
    
    LOOP_END = 10
    counter = 0 #accumulator
    total = 0
    
    #start the loop
    while counter < LOOP_END:
        #increment the accumulator
        counter += 1
        #while counter is < 10 these lines will execute
        print("The loop has run", counter, "times.")
        total += counter
        
        #output a message with the running total
        print("The total of this iteration is: ", total)
        #loop statement will return to the while statement

def loop2(): #example of a while loop
    #1oop2 accepts no arguments
    #loops through 10 times calculating a running total
    #outputs the total as it processes is
    
    LOOP_BEGIN = 1
    LOOP_END = 10
    total = 0
    
    #start the loop
    for number in range(LOOP_BEGIN, LOOP_END +1):
        #increment the accumulator
        #while num is between LOOP_BEGIN and LOOP_END +1
        print("The loop has run", number, "times.")
        total += number
        
        #output a message with the running total
        print("The total of this iteration is: ", total)
        #loop statement will return to the while statement
