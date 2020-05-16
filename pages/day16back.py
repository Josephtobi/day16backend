def prime():
    lis = []
    for i in range(2,72):
        if i % 1 == 0 and i % i == 0:
            valid = True
        for j in range(2,i//2+1):
            if i%j==0:
                valid=False
        if valid==True:
            lis.append(str(i))

    s=' '.join(lis)
    return(s)

