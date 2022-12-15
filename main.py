import re

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
    if (NeededNum % 3) == 0:
        return True
    else:
        return False

file = open('ilnur.txt')

'''Here we check all the given strings in the file'''


def FileWork(file):
    for i in file:

        match = re.findall(r"\b[01]+\b", i)
        if (match != []):
            for j in match:
                if (NumInSecBase(j) == True):
                    print(i)
                    break


        '''
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

                    
                ourNum = ''
            continue
        '''

FileWork(file)
file.close()
file.close()
