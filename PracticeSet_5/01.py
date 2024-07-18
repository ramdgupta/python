# Write a Python program to find the sum of all numbers in a list
def  listSum (num_list):
    sum =0
    for num in num_list:
        sum += num
    return sum

#print(listSum([1,2,3,4,5]))

# Write a function to check if a given number is prime or not.
def checkPrimeNum(num):
    if(num%2==0):
         return f"{num} is prime number"
         
    else:
       return f"{num} is not a prime number"

#print(checkPrimeNum(5))

#Write a Python program to find the factorial of a number using recursion
    


