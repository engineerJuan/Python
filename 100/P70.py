def  sustancia(ph):
    if ph < 7:
        return 'Acida'
    elif ph > 7:
        return 'Basica'
    else:
        return 'Neutra'
    
resultado = sustancia(7)
print(resultado)