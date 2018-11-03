import tensorflow as tf 
import os 
import pandas as pd 
import numpy as np
import keras 
from keras import models
from keras import layers



df = pd.read_csv("last_names/English.csv")
for file in os.listdir("last_names/"):
    if ".csv" in file:
        # apply something to file 
        if file == "English.csv":
            print("hit english, done nothing")
        else: 
            newdf = pd.read_csv("last_names/" + file)
            df = df.append(newdf)
        print(file)

eng_germ = df.ix[(df['origin'] == "English") | (df['origin'] == "German" )]
other = df.ix[(df['origin'] != "English") & (df['origin'] != "German")]   
df_rename = eng_germ.append(other)

df_rename = df_rename.drop('Unnamed: 0',1)
trn_p = 0.95
train_n = np.random.choice(df_rename.index.values,int(0.95*25463))
train = df_rename.ix[train_n]
test = df_rename.drop(train.index)

# Define simple model sequential model before I use a recurrent neural net. 
model = models.Sequential()
model.add(layers.Dense(32, input_shape= (1,)))
model.add(layers.Dense(20))
model.add(layers.Dense(10))
model.add(layers.Dense(1, activation= "softmax"))
print(model.summary())


# Need to arrange them, compile the model and run it etc. 






