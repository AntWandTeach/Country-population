from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

def init_Model(depth, categories):
    model = Sequential()
    model.add(Input(shape=(depth, categories)))
    model.add(LSTM(units= 20, activation= 'sigmoid'))
    model.add(Dense(categories, activation='sigmoid'))
    model.compile(loss= 'categorical_crossentropy', metrics= ['accuracy', 'mse'])
    return model

# def trainingAndSave(model, x_train, y_train):



