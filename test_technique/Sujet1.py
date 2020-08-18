def chaine(ch):

    Majiscule=""
    for i in range(len(ch)):
        if (ord(ch[i] )>= 97 and ord(ch[i] )<= 122):
                k  =ord(ch[i]) - 32

                Majiscule = Majiscule+chr(k)
        else:
            Majiscule=Majiscule+ch[i]


    return (Majiscule)
ch = input()
print(chaine(ch))