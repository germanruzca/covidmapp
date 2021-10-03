# German Ruiz to the NASA Space Challenge
# Octubre 2021
# @germanruzca

import pickle
from sklearn import svm
import pandas as pd

#Data name
file_path = './data/data.csv'

# Load the data
data = pd.read_csv(file_path)

# Separate the data
x = data[['POPULATION' , 'WEATHER', 'TIME','TYPE_PLACE','DAY','LAST_CASES']]
y = data['OUT']

# Load and fit the model
classifier = svm.SVC(kernel='rbf')
classifier.fit(x, y)

# Save the model
pickle.dump(classifier, open("model.pkl", "wb"))