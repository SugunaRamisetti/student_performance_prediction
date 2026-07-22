def get_prediction(model, input_data):
    """
    Takes a loaded model and preprocessed input data, 
    and returns the predicted score.
    """
    prediction = model.predict(input_data)[0]
    return prediction
