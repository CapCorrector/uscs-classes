###list
squares = [ n*n for n in range(10) ]


print(sum(squares))


### generator
squares = (n*n for n in range(10) )

print(sum(squares))
