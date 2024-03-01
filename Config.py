import os

num_of_categories = 100
depth_ = 5
begin_year = 1960
end_year = 2022

datasets_path = {}
models_path = {}
results_path ={}
tables_path = {}
path_id = [datasets_path, models_path, results_path, tables_path]
paths = ['datasets', 'models', 'results', 'tables']

for j in range(len(paths)):
    for dirs, folder, files in os.walk(paths[j]):
        for i in files:
            path_id[j][i[:i.index('.')]] = (paths[j] + '/' + i)
print(path_id)
