# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird

def find(n):
    if (n%2==0):
        if (n>1 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")
        elif (n>20):
            print("Not Weird")
    else:
        print("Weird")
if __name__ == '__main__':
    n = int(input().strip())
    find(n)
    

