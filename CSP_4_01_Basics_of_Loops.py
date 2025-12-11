#All questions must use a loop for full points.



def oddNumbers(n:int) ->str:
    result=""
    for i in range (1,n+1):
        if i%2!=0:
            result=result+str(i)+ " "
    return result.strip()

    # Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    # example oddNumbers(5) -> "1 3 5"
    # example oddNumbers(8) -> "1 3 5 7"
    # example oddNumbers(-8) -> ""

print(oddNumbers(3))
oddNumbers(5)

def backwards(n)-> str:
    if n<1:
        return""
    num=[]
    for i in range (n,0, -1):
        num.append(str(i))
    return" ".join(num)
print (backwards(10))

    # modify the below function such that it prints out all the numbers from n to 1
    # inclusive starting at n and counting down to 1
    # example backwards(5) -> "5 4 3 2 1"
    # example backwards(8) -> "8 7 6 5 4 3 2 1"
    # example backwards(-2) -> ""
    # """


import random
def randomRepeating():
    tries=0
    num=0
    while num!=10:
        num=random.randint(1,10)
        tries+=1
        print (num)
    print("it took "+str(tries)+" times to roll a 10")
randomRepeating()




    # Print out a random number from 1-10 until you get a 10. Then print out how many
    # times it took to roll a 10
    # NOTE: Given randomness no test for this question


import random
def randomRange(n):
    lowest=100
    highest=0
    for i in range(n):
        num=random.randint(1,100)
        print(num)
        if num>highest:
            highest=num
        if num<lowest:
            lowest=num
    print("highest:"+str(highest))
    print("lowest:"+str(lowest))
randomRange(10)

    # Generate a random number from 1 to 100 n number of times. Then after that is
    # done print out what the highest number and the lowers number was from the rolled numbers.
    # NOTE: Given randomness no test for this question

def reverse(word:str)->str:
    result=""
    for i in range(len(word)-1, -1,-1):
        result=result+word[i]
    return result
print(reverse("hello"))#example


    # Takes in a string as an argument and return the given string in reverse.
    # example reverse("cat") -> "tac"
    # example reverse("Hello") -> "olleH"


def fizzBuzzContinuous(n):
    result=""
    for i in range(1,n+1):
        if i %3==0 and i%5==0:
            result+="fizzbuzz "
        elif i % 3 == 0:
            result+="fizz "
        elif i%5==0:
            result+="buzz "
        else:
            result+=str(i)+" "
    return result.strip()
print(fizzBuzzContinuous(20))


    # Modify the function such that it does the fizzbuzz operation on all numbers
    # from 1 to n(inclusive).
    # Fizz buzz is defined as
    # if the number is divisble by 3 print fizz
    # if the number is divisible by 5 print buzz
    # if the number is divisible by both 3 and 5 print fizzbuzz
    # if none of the above apply print the number.
    #
    # As with above questions add each anseer to a string and return the final string.




def collatz(n):
    sequence=str(n)
    while n!=1:
        if n%2==0:
             n=n//2
        else:
            n=3*n+1
        sequence+=" "+str(n)
    return sequence
print(collatz(6))

    # Modify this function such that it mimics the collatz conjecture starting at n
    # and prints out each number.
    # The collatz conjecture is that if n is an even number divide it by 2. if n is
    # an odd number multiply it by 3 and add 1.
    # Repeat this process until n == 1.




def fibonacci(n):
    if n<=0:
        return""
    sequence="0"
    if n>1:
        a,b=0,1
        sequence+=" 1"
        count=2
        while count<n:
            nextnumber=a+b
            sequence+=" "+str(nextnumber)
            a,b=b,nextnumber
            count+=1
    return sequence
print(fibonacci(6))

    # for the given argument n print out the first n numbers of the fibonacci
    # sequence in a single string sperated by spaces.
    # The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    # the first two numbers. Every subsequent number is the prior two numbers added together.
    # Example fibonacci(6) -> "0 1 1 2 3 5"
    # Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    # Example fibonacci(1) -> "0"