def loopPrintPower():
    """
    1.Problem (Loops)
    https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
    read and set , integer,n, from STDIN. 
    For all non-negative integers i < n , print pow(i,2).
    
    """
    n=int(input("Enter the value : "))
    for i in range(n):
        print(pow(i,2))

def main():

    loopPrintPower()
    
main()