import csv

import numpy
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, LSTM, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from Config import *
from pandas import *

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
    filename = directories['models'] + 'model_' + model_name
    model.save(filename)

def load_Model(model_name= '0'):
    return keras.models.load_model(directories['models']+'model_'+model_name)
def predict_results(model, x_test, predict_name = '0'):
    prediction = model.predict(x_test)
    with open(directories['predictions'] + 'pre_' + predict_name + '.csv', mode= 'w') as file:
        file_wr = csv.writer(file, delimiter=",", lineterminator="\r")
        for i in range(end_year - begin_year + 1):
            file_wr.writerow([x_test[i], numpy.argmax(prediction[i, :])])

# def Predict_format()
if __name__ == '__main__':
    model = init_Model(depth_, num_of_categories)
    print(model.summary())

