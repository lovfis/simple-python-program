#Below we've started a class called FibSeq. At any time,
#FibSeq holds two values from the Fibonacci sequence:
#back1 and back2.
#
#Create a new method inside FibSeq called next_number. The
#next_number method should:
#
# - Calculate and return the next number in the sequence,
#   based on the previous 2.
# - Update back2 with the former value of back1, and update
#   back1 with the new next item in the sequence.
#
#This means that consecutive calls to next_number should
#yield each consecutive number from the Fibonacci sequence.
#Calling next_number 5 times would print 1, 2, 3, 5, and 8.


class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
        
    def next_number(self):
        new_number = self.back1 + self.back2
        self.back2 = self.back1
        self.back1 = new_number
        return new_number
        

#The code below will test your method. It's not used for
#grading, so feel free to change it. As written, it should
#print 1, 2, 3, 5, and 8.
newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())


