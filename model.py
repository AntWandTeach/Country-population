from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, LSTM, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from Config import *

def init_Model(depth, categories):
    model = Sequential()
    model.add(Input(shape=(depth, categories)))
    model.add(Dropout(dropout_ratio))
    model.add(LSTM(units= input_size_lstm, activation= 'sigmoid'))
    model.add(Dropout(dropout_ratio))
    model.add(Dense(categories, activation='sigmoid'))
    model.compile(loss= 'categorical_crossentropy', metrics= ['accuracy', 'mse'])
    return model

def trainingAndSave(model, x_train, y_train, model_name = '0'):
    model.fit(x_train, y_train, epochs= nums_epochs, validation_split = valid)
    filename = 'models/model_' + model_name
    model.save(filename)


