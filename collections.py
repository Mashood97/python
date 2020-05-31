#dictionaries:
mashood = {}
mashood['first'] = 'Mashood'
mashood['last']='Siddiquie'


Urooj= {}
Urooj['first'] = 'Urooj'
Urooj['last']='Parekh'


#lists:

people = []
people.append(mashood)
people.append(Urooj)

people.append({
    'first': 'Qirat',
    'last': 'Parekh'
})

print(people)