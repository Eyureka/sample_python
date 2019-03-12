#PF-Tryout
from threading import Thread
def func1():
    result_sum=0
    #Write the code to find the sum of numbers from 1 to 10000000
    for i in range(0,10000000):
        result_sum+=i
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    #Write the code to accept 5 numbers from user and find its sum
    for i in range(0,5):
        print 'enter number ',i+1,": "
        result_sum+=input()
    print("Sum from func2:",result_sum)

#Modify the code given below to execute func1() and func2() in two separate threads
thread1=Thread(target=func1)
thread1.start()
thread2=Thread(target=func2)
thread2.start()
thread1.join()
thread2.join()