import os
import numpy as np
import random

# use 80% data to train and 18% to validate per class
def load(data_path, classes, train_percent=0.80):
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    for class_txt in classes:
        texts = []
        labels = []
        path = os.path.join(data_path, class_txt)
        for fname in sorted(os.listdir(path)):
            if fname.endswith('.txt'):
                with open(os.path.join(path, fname), encoding="utf8") as f:
                    texts.append(f.read())
                labels.append(classes[class_txt])
        
        seed = random.randint(0, 100)
        random.seed(seed)
        random.shuffle(texts)
        random.seed(seed)
        random.shuffle(labels)

        num = int(len(labels) * train_percent)
        
        train_data += texts[:num]
        train_labels += labels[:num]
        test_data += texts[num:]
        test_labels += labels[num:]

    return (train_data, train_labels), (test_data, test_labels)

