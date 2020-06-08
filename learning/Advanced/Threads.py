from threading import *
from time import sleep

class A(Thread): #(Thread) makes the class a thread class
    def run(self):
        for i in range (5):
            print("hello")
            sleep(1)

class B(Thread): #(Thread) makes the class a thread class
    def run(self):
        for i in range (5):
            print("hi")
            sleep(1)

a = A()
b = B()
a.start() # we cannot call the run method directly, if we call like that it would be executed in normal way
          # not parallely using threads. Secondly run method is a method of thread class, and we have to
          # override the run method for parallel execution. We cannot have any other method
print("sleep of 0.2 seconds after the start of thread a and before the start of thread b")
sleep(0.2) # sleep of 0.2 seconds to make it parallel and one after another
b.start()
sleep(0.2)
print("main thread is waiting for thread a and b")
a.join() # informs the main thread that it has to wait for thread a
b.join() # informs the main thread that it has to wait for thread b
print("finally all completed bye !!!")