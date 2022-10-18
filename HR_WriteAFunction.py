def leapYear(year):
    """
    2.Problem (Write a function)
    https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
    read the year and 
    Find the Leap Year ( True/False)
    """
    leap=False
    if (year >=1900) and (year <= 100000):
        if(year % 4 == 0):
         if (year % 100 !=0 or year % 400 == 0):
            leap = True

    return leap

def main():

   
    year=int(input("Enter the year"))
    print(leapYear(year))

    

main()