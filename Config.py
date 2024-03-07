import os

num_of_categories = 100
depth_ = 5
begin_year = 1960
end_year = 2022

directories = {'datasets': 'datasets/', 'models': 'models/', 'results':'results/', 'tables': 'tables/' }
# params for model
valid = dropout_ratio = 0.2
input_size_lstm = 20
nums_epochs = 10