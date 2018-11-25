from flask import Flask, jsonify, request, json
from flask_cors import CORS
from tensorflow.python.keras import models
import tensorflow as tf
import pickle

vectorizer = pickle.load(open("./model/vectorizer.pickle", "rb"))
selector = pickle.load(open("./model/selector.pickle", "rb"))
new_model = models.load_model('./model/MyModel.h5')
graph = tf.get_default_graph()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def main():
    data = json.loads(request.data)
    x_val = vectorizer.transform([data['content']])
    x_val = selector.transform(x_val).astype('float32')

    with graph.as_default():
        result = new_model.predict(x_val)

    return jsonify({
        'result': result[0].tolist(),
        'classes': ['Congnghe (Tech)', 'Suckhoe (Health)', 'Thethao (Sport)', 'Xe (Car & motor)']
    })