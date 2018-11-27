# vietnamese-text-classification

Demo: http://45.77.173.11:8080

Crawl data from vnexpress, zing news and vietnamese and use Multi-layer perceptron model to classify all. You can find all data in `./data`

https://developers.google.com/machine-learning/guides/text-classification/step-2-5

# Installation
python3 is required

    pip3 install -r requirements.txt

Download dataset: https://drive.google.com/file/d/1gY2fPjGElSXVN83syW5bDmxWS7sdu2Hh/view?usp=sharing

# Train model

    python3 train_model.py

After finished, The model will be stored in `./model/MyModel.h5`

`./model/selector.pickle` and `./model/vectorizer.pickle` are used to vectorize the input data

Pre-trained model: https://drive.google.com/file/d/1rObNGFWEbkaD2sE9NBsf8RUyTLLElNBq/view?usp=sharing


# Use Model to predict


View `predict.py` file

    python3 predict.py


The result will be look like: `[[0.0050260744 0.99930882 0.0016016784 0.000028327899]]`

It means 99.9% that it is in class 1

# Run HTTP Server
    cd ./http-server

    FLASK_APP=main.py flask run

    cd react-client

    yarn

    yarn dev