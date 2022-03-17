def rajouter_les_fleches(nb):
    mychr = ""
    while nb != 0 :
        if nb > 0 : 
            nb = nb-1
            mychr += "<"
        if nb < 0 : 
            nb = nb+1
            mychr += ">"
    return mychr

def rajouter_les_nombres(nb):
    mychr = ""
    while nb != 0 :
        if nb > 0 : 
            nb = nb-1
            mychr += "+"
        if nb < 0 : 
            nb = nb+1
            mychr += "-"
    return mychr


def brainfuckEncodding(text):
    
    listOfChr = set(text)

    listOfChr = {ord(ch) for ch in listOfChr}


    emplacementDesCellules = [nombreAsciiLettre//8 for nombreAsciiLettre in listOfChr]
    emplacementDesCellules = sorted(set(emplacementDesCellules)) 
    


    bfText = "++++++++"
    bfText += "["
    endLoop = ""
    for i in range(len(emplacementDesCellules)):
        endLoop += "<"
        bfText += ">"
        for j in range(emplacementDesCellules[i]):
            bfText += "+"
    endLoop += "-]"
    bfText += endLoop

    emplacementDesCellules = [index*8 for index in emplacementDesCellules]

    currentIndex = 0 
    for i in range(len(text)):
        idxCell = 0
        minVal  = float('inf')
        for j in range(len(emplacementDesCellules)):
            if ((ord(text[i]) - emplacementDesCellules[j])**2)**0.5  < minVal :
                idxCell = j+1
                minVal = ord(text[i]) - emplacementDesCellules[j]

        
        
        bfText += rajouter_les_fleches(currentIndex - idxCell) + rajouter_les_nombres(minVal) + "."
        currentIndex = idxCell
        emplacementDesCellules[currentIndex-1] += minVal
        
    return bfText


text = input("inserez votre texte en ascii : ")
print(brainfuckEncodding(text))


