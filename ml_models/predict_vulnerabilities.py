import pickle

def load_model():
    with open('models/vulnerability_model.pkl', 'rb') as file:
        return pickle.load(file)

def predict(code_features):
    model = load_model()
    return model.predict([code_features])
