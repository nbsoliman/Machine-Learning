import pandas as pd

data = pd.read_csv("Smarket2.csv")
print("--------------------------Display Data----------------------------------")
print(data.head(1250))
print("--------------------------Display Shape---------------------------------")
print("Shape: ", data.shape)
print("--------------------------Extract Features------------------------------")