from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
import numpy
def init_Model():
    model = Sequential()
