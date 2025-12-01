def findDictionary(dataList, key, value):
    info = {}
    for i in range(len(dataList)):
        if dataList[i].get(key) == value:
            info["index"] = i
            info["data"] = dataList[i]
            break
    return info