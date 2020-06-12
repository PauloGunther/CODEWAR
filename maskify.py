def maskify(text):   
    i = len(text) - 4
    return text.replace(text[0:-4], '#'*i)


maskify('teste meu gato')
