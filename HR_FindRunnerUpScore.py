def findRunnerUp():
    """
    5.Problem (Find the Runner-Up Score)
    https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
    
    """
    n = int(input("n: "))
    arr = list(map(int, input("list of Scores: ").split()))
    
    s = set(arr)
    r = sorted(list(s))
    print(r[-2])

def main():

    findRunnerUp()
   
main()
