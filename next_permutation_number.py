## Without using the inbuilt permutation function-This is a Python Program to receive the dynamic number input and prints the next greater number than the input number among the shuffled permutation ways of the given input number

def ways(n):
    """
    This function return the list of all possible shuffled permutations of the passed parameter n

    :param n: integer
    :return: list of all possible shuffled permutations of the passed parameter n
    """
    if len(n)==0:
        return []
    elif len(n)==1:
        return(n)
    else:
        l=[]
        for i in range(len(n)):
            temp=n[i]
            fin=n[:i]+n[i+1:]
            for j in ways(fin):
                l.append(str(temp)+str(j))
            print("  {}".format(l))
        l=[int(x) for x in l]
        return(l)

n=input("input:")


p=sorted(list(set((ways(n)))))
print(p)
for k in range(len(p)):
    if p[k]==int(n):
        print(k,'--')
        print(p[k])
        print(p[k+1])  # prints the next greater number than the input number among the shuffled permutation ways of the given input number
