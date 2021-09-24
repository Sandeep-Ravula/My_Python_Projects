def compareDict(dict1,dict2):
    decision=True
    for every in dict2:
        print(every)
        decision=(every in dict1)
        if decision==True:
            pass
        elif decision==False:
            break
    if decision==True:return('satisfied')
    elif decision==False:return('not satisfied')

print(compareDict(input('enter dictionary 1:'),input('enter dictionary 2:')))