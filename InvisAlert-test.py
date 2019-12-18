# print string - Hello Invisalert!
print('Hello, Invisalert!')

# sum of num1 and num2
num1 = 42
num2 = 12
sum = num1 + num2
print ("Sum of",num1,"and",num2,"is",sum)

# product of num1 and num2
product = num1 * num2
print ("Product of",num1,"and",num2,"is",product)

# Largest number in array [10, 427, 12, 80, 572]
array = [10, 427, 12, 80, 572]
length = len(array)
# python function to find largest 
def largestInArray(array, length): 
  
    # define initial value of largest
    largest = array[0] 

    # loop through array elements from second and compare with every element
    for i in range(1, length): 
        if array[i] > largest: 
            largest = array[i] 
    return largest
  
result = largestInArray(array,length) 
print ("Largest in given array is",result)

# palindrome
# given a string, reverse the string and check to match the original string
def palindrome(str):
    reverseStr = str[::-1]
    if (str == reverseStr):
        return str + " is a palindrome"
    return str + " is not a palindrome"

string = "racecar"
palindromeTest = palindrome(string)
print (palindromeTest)