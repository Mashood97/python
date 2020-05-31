# amount = input('How much did you pay? ')

# amount = float(amount)
# if amount >=1.00: 
#     tax = .07

# else:
#     tax = 0

# print('The tax is: ' + str(tax))



# country = input('Enter your country name? ')


# if country.lower() == 'pakistan':
#     print('Oh A Pakistani')
# else:
#     print('youre not a pakistani')    


#multiple if else:

# country = input('Which country you live in? ')

# tax = 0 

# if province.lower() == 'sindh':
#     tax = 0.5

# if province.lower() == 'sindh' or province.lower() == 'balochistan':
#     tax = 0.5

# if(country.lower() == 'pakistan'):
#     province =input('What province do you live in? ')

#     if province.lower()in('sindh','balochistan'):
#         tax = 0.5
#     elif province.lower() == 'punjab':
#         tax = 0.13

#     elif province.lower() == 'pakhtun':
#         tax = 0.3
#     else: 
#         tax = 0.15

#     output = f'The tax of country: {country} of {province} is {str(tax)}'
#     print(output)

# else:
#     tax = 0
#     output = 'The tax is not allowed outside of Pakistan so tax is: '+ str(tax)
#     print(output)            


#complex conditions with boolean too:


grade_point = float(input('whats your avg grade point? '))
lowest_grade = float(input('whats your lowest grade ?'))

isMadeHonour = False

if grade_point >=.85 and lowest_grade >=.70:
    isMadeHonour = True

else:
    isMadeHonour = False

if(isMadeHonour): print('You made an honour roll')
else: print('no you havent made the honour roll')