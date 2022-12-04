file = open('ilnur.txt')
'''     the NumInSecBase finds out if the number fits the conditions '''
def NumInSecBase(i):
    i = i[::-1]
    lengthOfi = len(i) - 1
    NeededNum = 0
    while (lengthOfi >= 0):
        if (i[lengthOfi] != '0') and (i[lengthOfi] != '1'):
            return False
        NeededNum += int(i[lengthOfi])*(pow(2,lengthOfi))
        lengthOfi -=1
    #print(needednum)
    if (NeededNum % 3) == 0:
        return True
    else:
        return False
#print(NumInSecBase('111111111111111111'))
file = open('ilnur.txt')
'''Here we check all the given strings in the file'''
def FileWork(file):
    for i in file:
        ourCurrentString = i
        ourNum = ''
        for j in (i+' '):
            try:
                int(j)
                ourNum += j
                #print(ourNum)
            except ValueError:

                if (ourNum != ''):
                    if (NumInSecBase(ourNum) == True):
                        print(ourCurrentString)
                        ourCurrentString = ''
                        break

                    #print('ur fucked huh!!!!!!!!')
                ourNum = ''
            continue


FileWork(file)
file.close()

'''
so....
1) if 1-9: begin a cycle where count until NOT 0-9 number
2) else: continue
NumFinder:
sooooooo number should num % 3 == 0. ok. then we have to deal with it being in the 2 number base.
'''









file.close()