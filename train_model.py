# Created by nghiatrx
# After trained, the Model will be stored in the 'model' folder

import mlp_model
import load_data
import random

data = load_data.load(
    data_path='data', 
    classes={'congnghe': 0, 'suckhoe': 1, 'thethao': 2, 'xe': 3}, 
    seed=random.randint(1, 1000))

train_percent = 0.82 # use 82% data to train and 18% to validate
number_samples_train = int(len(data[0]) * 0.82)

(data_train, labels_train) , (data_test, labels_test) = (data[0][0:number_samples_train], data[1][0:number_samples_train]), (data[0][number_samples_train:], data[1][number_samples_train:])

mlp_model.train_ngram_model(data=((data_train, labels_train) , (data_test, labels_test) ), dropout_rate=0.2, epochs=3000)


