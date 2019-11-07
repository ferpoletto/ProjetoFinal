class Utils:

    def gera_dict(self, data):
        self.list = []
        for i in range(len(data)):
            aux = {"ID": data[i][0],
                          "hits": data[i][1],
                          "url": data[i][2],
                          "shorturl": data[i][3]}
            self.list.append(aux)
        return self.list