def maskify(text):   
    i = len(text) - 4
    print(text.replace(text[0:-4], '#'*i))
    pass 


maskify('teste meu gato')
