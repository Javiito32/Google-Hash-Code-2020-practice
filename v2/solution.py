def solve(fileName):

    def points(array):
        asol = []
        _x = 0
        for i in range(0, len(array)):
            if array[i] > 0:
                asol.append(i)
        for x in asol:
            _x += slicesPerType[x]
        return _x
        

    f = open(fileName+".in", "r")
    data = f.read()
    data = data.split()
    maxSlices = int(data[0]) #maximo numero de slices
    _maxSlices = int(maxSlices)
    pizTypes = int(data[1]) #numero de tipos de pizza
    pizTypes -= 1
    slicesPerType = [] #slides segun el tipo de pizza
    qttyPerType = []
    for i in range(2, len(data)):
        slicesPerType.insert(i-2 , int(data[i]))
        qttyPerType.insert(i-2, 0)

    _qttyPerType = qttyPerType.copy()
    HighScore = 0
    for A in range(len(qttyPerType)):
        qttyPerType = _qttyPerType.copy()
        _maxSlices = maxSlices

        for i in range(pizTypes-A, -1, -1):

            _maxSlices -= slicesPerType[i]

            if _maxSlices == 0:
                qttyPerType[i] += 1
                break

            if _maxSlices < 0:
                _maxSlices += slicesPerType[i]
                continue

            if _maxSlices > 0:
                qttyPerType[i] += 1
                continue

        if _maxSlices == 0:
            finalqtty = qttyPerType.copy()
            break
        else:
            if points(qttyPerType) > HighScore:
                finalqtty = qttyPerType.copy()
                HighScore = points(qttyPerType)

    qttyPerType = finalqtty.copy()

    #for i in range(pizTypes, -1, -1):     
    #
    #    if qttyPerType[i] == 1:
    #        acum.append(i)
    #        tmpSum = 0
    #        for a in acum:
    #            tmpSum += slicesPerType[a] 
    #            tmpSum += slicesPerType[i]
    #            tmpSum += _maxSlices
    #            for z in slicesPerType:
    #                if tmpSum <= z:
    #                    print("Alcanzo")                    
    #                    for y in range(pizTypes, -1, -1):
    #                        if slicesPerType[y] == slicesPerType:
    #                            qttyPerType[y] += 1
    #                            qttyPerType[a] -= 1
    #            tmpSum -= slicesPerType[i]
    #            tmpSum -= _maxSlices

                



    def decode(sol):
        asol = []
        _x = 0
        for i in range(0, len(sol)):
            if sol[i] > 0:
                asol.append(i)
        o = open("out/"+fileName+".out", "w")
        o.write(str(len(asol)) + "\n")
        for i in asol:
            o.write(str(i)+" ")
        for x in asol:
            _x += slicesPerType[x]
        print("Puntuación: " + str(_x))
        o.close()
                
    decode(qttyPerType)  

files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]  
for x in files:
    solve(x)