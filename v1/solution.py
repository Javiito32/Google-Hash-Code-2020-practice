def solve(fileName):
    f = open(fileName+".in", "r")
    data = f.read()
    data = data.split()
    print(data)
    maxSlices = int(data[0]) #maximo numero de slices
    _maxSlices = int(maxSlices)
    pizTypes = int(data[1]) #numero de tipos de pizza
    pizTypes -= 1
    slicesPerType = [] #slides segun el tipo de pizza
    qttyPerType = []
    for i in range(2, len(data)):
        slicesPerType.insert(i-2 , int(data[i]))
        qttyPerType.insert(i-2, 0)


    for i in range(pizTypes, -1, -1):

        _maxSlices -= slicesPerType[i]

        if _maxSlices == 0:
            qttyPerType[i] += 1
            print("end")
            break

        if _maxSlices < 0:
            print("ñe")
            _maxSlices += slicesPerType[i]
            continue

        if _maxSlices > 0:
            qttyPerType[i] += 1
            print("sumo")
            continue

    print(qttyPerType)

    def decode(sol):
        asol = []
        for i in range(0, len(sol)):
            if sol[i] > 0:
                asol.append(i)
        o = open("out/"+fileName+".out", "w")
        o.write(str(len(asol)) + "\n")
        for i in range(0, len(asol)):
            o.write(str(asol[i])+" ")
        o.close()
                
    decode(qttyPerType)  

files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]  
for x in files:
    solve(x)