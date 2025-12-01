from json import dumps, load, decoder

def readFile(fileName):
    try:
        fileData = None
        with open(fileName) as f:
            fileData = load(f)
            f.close()
        return fileData
    except:
        return []
    

def saveFile(fileName, data):
    jsonFile = open(fileName, "w")
    jsonFile.write(dumps(data))
    jsonFile.close()
    print("Datos guardados con exito")
    