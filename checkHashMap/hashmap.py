class HashMap:
    def __init__(self, dic):
        self.dic = dic

    def getItems(self, key):
        return self.dic.get(key)

    def addItems(self, key, item):
        self.dic[key] = item
        return True

    def deleteItems(self, key):
        self.dic.pop(key)
        return True

    def getAllItem(self):
        print(self.dic)