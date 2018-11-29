from flask import Flask, jsonify, request, json
from flask_cors import CORS
from tensorflow.python.keras import models
import tensorflow as tf
import pickle

vectorizer = pickle.load(open("./model/vectorizer.pickle", "rb"))
new_model = models.load_model('./model/MyModel.h5')
graph = tf.get_default_graph()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def main():
    data = json.loads(request.data)
    x_val = vectorizer.transform([data['content']])

    with graph.as_default():
        result = new_model.predict(x_val)

    return jsonify({
        'result': result[0].tolist(),
        'classes': [
            'Cong-nghe (tech)', 
            'Suc-khoe (health)', 
            'The-thao (sport)', 
            'Xe (Car & motor)',
            'Am-nhac (music)',
            'Du-lich (travel)',
            'Giao-duc (education)',
            'Kinh-doanh (business)',
            'Phap-luat (law)'
            'Phim (Movie)',
            'Thoi-su (News)',
            'Thoi-trang (Fashion)'
        ]
    })