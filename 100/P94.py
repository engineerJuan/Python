cadenas =  ['Python', 'Sql', 'Html', 'Css', 'Java Script', 'Php', 'Java']
caracter = 'a'

con_a = list(filter(lambda x : caracter in x, cadenas))

print(cadenas)
print(con_a)