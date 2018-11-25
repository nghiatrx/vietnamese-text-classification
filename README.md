# vietnamese-text-classification

Demo: http://45.77.173.11:8080

Crawl data from vnexpress, zing news and vietnamese and use Multi-layer perceptron model to classify all. You can find all data in `./data`

https://developers.google.com/machine-learning/guides/text-classification/step-2-5

# Installation
python3 is required

    pip3 install -r requirements.txt

# Train model

    python3 train_model.py

After finished, The model will be stored in `./model/MyModel.h5`


`./model/selector.pickle` and `./model/vectorizer.pickle` are used to vectorize the input data

Read more: https://developers.google.com/machine-learning/guides/text-classification/step-3

# Use Model to predict


View `predict.py` file

    python3 predict.py


The result will be look like: [[0.0050260744 0.99930882 0.0016016784 0.000028327899]]

It means 99.9% that it is in class 1. Currently, we have 4 classes. class 0: congnghe (tech), class 1: suckhoe (health), class 2: thethao (sport), class 3: xe (car & motor)

# Run HTTP Server
    cd ./http-server

    FLASK_APP=main.py flask run

    cd react-client

    yarn

    yarn dev