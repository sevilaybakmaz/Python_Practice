def loopPrintNumber():
    """
    3.Problem (Print Function)
    https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
    """
    n=int(input("Enter the value : "))
    if(n>=1) and (n<=150):
        for i in range(1,n+1):
            print(i,end=" ")

def main():

   

    loopPrintNumber()
    

main()