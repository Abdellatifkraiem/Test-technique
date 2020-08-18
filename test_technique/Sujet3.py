def voisinsCase(plateau ,i,j):
    l=[]
    if i == 0 :
        if j ==0 :
            if plateau[i + 1][j] == False:
                l.append((i + 1, j))
            if plateau[i][j + 1] == False:
                l.append((i, j + 1))
        if j ==len(plateau[0])-1:
            if plateau[i ][j-1] == False:
                l.append((i , j-1))
            if plateau[i+1][j] == False:
                l.append((i+1, j ))
        else:
            if plateau[i][j + 1] == False:
                l.append((i, j + 1))
            if plateau[i][j - 1] == False:
                l.append((i, j - 1))
            if plateau[i + 1][j] == False:
                l.append((i + 1, j))
    if i == 1 :
        if j == 0:
            if plateau[i - 1][j] == False:
                l.append((i - 1, j))
            if plateau[i][j + 1] == False:
                l.append((i, j + 1))
        if j == len(plateau[1]) - 1:
            if plateau[i][j - 1] == False:
                l.append((i, j - 1))
            if plateau[i -1][j] == False:
                l.append((i - 1, j))
        else:
            if plateau[i-1][j]== False:
                l.append((i-1,j))
            if plateau[i][j+1]==False:
                l.append((i,j+1))
            if plateau[i][j -1] == False:
                l.append((i ,j-1))
    return(l)

def voisinsCases(plateau,listeCase):
    listResult=[]

    for i in listeCase:

        l = voisinsCase(plateau, i[0], i[1])

        for k in l :

            listResult.append(k)

    return (listResult)


def accessibles ( plateau,i,j):
   resulta =  voisinsCase(plateau, i, j)

   accessibl = voisinsCases(plateau,resulta)
   accessibl2 = voisinsCases(plateau,accessibl)
   k = accessibl+accessibl2
   listfinal =list(set(k))
   return k2


def chemin(plateau,i_Debut,j_Debut,k_Fin,r_Fin):
    if (k_Fin,r_Fin) in accessibles(plateau,i_Debut,j_Debut):
        return True
    else:
        return False

plateau=[[True,False,False,False],[False,True,True,False]]
print(chemin(plateau,1,3,0,1))