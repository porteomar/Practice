def string_splosion(str):
    newStr = ''
    j = 1

    for i in range(len(str)):
        newStr += str[0:j]
        j += 1

    return newStr

print string_splosion("omar")
