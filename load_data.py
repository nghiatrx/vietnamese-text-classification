import os
import numpy as np
import random

def load(data_path, classes, seed=1, max_len=None):
    texts = []
    labels = []
    for class_txt in classes:
        path = os.path.join(data_path, class_txt)
        count = 0
        for fname in sorted(os.listdir(path)):
            if fname.endswith('.txt'):
                if count == max_len:
                    break
                count += 1
                with open(os.path.join(path, fname), encoding="utf8") as f:
                    texts.append(f.read())
                labels.append(classes[class_txt])

    random.seed(seed)
    random.shuffle(texts)
    random.seed(seed)
    random.shuffle(labels)

    return texts, np.array(labels)

