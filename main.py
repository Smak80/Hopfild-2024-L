from DataLoader import DataLoader
from HopfildNN import HopfildNN as hopnn

d = DataLoader("train.bmp")
data = d.get_data()
h = hopnn()
h.train(data)

td = DataLoader("test.bmp")
test = td.get_data()
res = h.predict(test)
print(res)