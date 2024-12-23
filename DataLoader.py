import openpyxl as xl
from PIL import Image
import numpy as np

class DataLoader:
    def __init__(self, filename, data_size=(100, 100)):
        img = Image.open(filename).convert('L')  
        img_array = np.array(img)  
        self.__train_set = [
            [
                1 if img_array[y, x] == 0 else -1  
                for y in range(data_size[0])  
                for x in range(k * data_size[1], (k + 1) * data_size[1])  
            ] for k in range(3)  
        ]

    def get_data(self):
        return self.__train_set.copy()