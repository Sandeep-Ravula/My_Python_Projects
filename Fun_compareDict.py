def compareDict(nested_Dictionary):
    for key,value in nested_Dictionary.items():
        if type(value)=='dict':
            print(value)
            print(compareDict(value))
        elif type(value)=='list':
            for i in value:
                if type(i)=='dict':
                    print(compareDict(i))
                else:print(key,i.value())
        else:print(key,'-----',value,'-------')