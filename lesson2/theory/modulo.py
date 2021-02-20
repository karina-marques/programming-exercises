# The modulo operation (%) between two integer numbers n and m, written like
# x = n % m
# Returns the remainder of the integer division between n and m
# An important property of this operation is that the values that it can return
# are always between 0 and m-1.
# The modulo can be used to check divisibility by a number. Below there is an example of this
# with the number 2

x = int(input("Insert an integer number: "))

if x%2 == 1:
    print (str(x), 'is odd.')
else:
    print (str(x), 'is even.')