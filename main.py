terms=10
result=list(map(lambda x:2**x,range(terms)))
print("The total terms is :",terms)
for i in range(terms):
    print("2raised to power",i,"is",result[i])
