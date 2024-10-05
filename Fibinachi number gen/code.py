#fibinachi sequence gen
import time
stop = int(input("How far will you go?: "))
number1 = 0
number2 = 1
sequence_num = 0
for i in range(stop):
    sequence_num += 1       
    result = number1 + number2
    number1 = number2
    number2 = result
    #print("Sequence number: " +str(sequence_num) + "\nFibinachi number: " + str(result) + "\n")#, end = "\r")

print("Sequence number: " +str(sequence_num) + "\nFibinachi number: " + str(result) + "\n")#, end = "\r")
