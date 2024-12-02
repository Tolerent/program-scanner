from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data, labels):
    model = RandomForestClassifier()
    model.fit(data, labels)
    with open('models/vulnerability_model.pkl', 'wb') as file:
        pickle.dump(model, file)
