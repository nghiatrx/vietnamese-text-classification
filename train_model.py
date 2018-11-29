# Created by nghiatrx
# After trained, the Model will be stored in the 'model' folder

import mlp_model
import load_data
import random
import explore_data

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

(train_data, train_labels), (test_data, test_labels) = load_data.load(
    data_path='data',
    train_percent=0.80,
    classes={
        'congnghe': 0,
        'suckhoe': 1,
        'thethao': 2,
        'xe': 3,
        'amnhac': 4,
        'dulich': 5,
        'giaoduc': 6,
        'kinhdoanh': 7,
        'phapluat': 8,
        'phim': 9,
        'thoisu': 10,
        'thoitrang': 11
    }
)

mlp_model.train_ngram_model(data=((train_data, train_labels), (test_data, test_labels)), num_classes=12, dropout_rate=0.2, epochs=100)


