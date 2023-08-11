examp = (i for i in range(10))
print(examp) #it displays generator object, because expression above return such a object

#to display number we should add for loop and pass the generator object there
for num in examp:
    print(num)

