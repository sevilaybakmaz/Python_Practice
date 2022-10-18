def loopListComprehension():
    """
    4.Problem (List Comprehension)
    """
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    n = int(input("n: "))
    arr=[]
    for k in range(x+1):
        for j in range(y+1):    
            for i in range(z+1):
                if (i+j+k)!=n:
                    arr.append([k,j,i])

                else:
                    pass

    print(arr)

def main():

  
    loopListComprehension()

main()