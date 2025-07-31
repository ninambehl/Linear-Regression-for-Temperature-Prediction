import pickle as pkl
import joblib as jb

def predict(data):
    # with open("linear_model.pkl", "rb") as file:
    #     loaded_model = pkl.load(file)
    loaded_model = jb.load("./linear_model.pkl")
    predictions = loaded_model.predict(data)
    return predictions