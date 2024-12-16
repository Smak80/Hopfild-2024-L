from DataLoader import DataLoader
from HopfildNN import HopfildNN as hopnn

d = DataLoader("data.xlsx")
data = d.get_data()
h = hopnn()
h.train(data)

td = DataLoader("test.xlsx")
test = td.get_data()
res = h.predict(test)
print(res)