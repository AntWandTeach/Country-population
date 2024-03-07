import matplotlib.pyplot as plt
import pandas as pd
import Config


def plot_grap(file, predicted_values=None):
    data = pd.read_csv(file_path)


    Time = data['Time']
    original = data['Population']
    if predicted_values:
        plt.plot(Time, predicted_values, color='red', label='Predicted Values')

    plt.plot(Time, original, color='blue', label='Original Values')
    plt.axis((Config.begin_year, Config.end_year, 0, 1000000))
    plt.title('Time Series Data')
    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.show()
    # plt.title


file_path = 'datasets/new.csv'
predicted_values = pass
plot_grap(file_path, predicted_values)
