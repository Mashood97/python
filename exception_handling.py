x = 42
y = 0


print()
try:
    print( x / y)

except ZeroDivisionError as e:
    print('Cant divide by zero')
else:
    print('Something went wrong in else')
finally:
    print('CLeanup code')

print()