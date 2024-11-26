import os
import pickle
import tensorflow as tf

config = {
    'stress': {
        'scalar_file': 'production/standard_scaler.pkl',
        'ANN': 'production/stress_detection_model.h5'

    }}

dir = os.path.dirname(__file__)

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load( open(os.path.join(dir, filepath), "rb" ) )
    return None

def GetStandardScalarForStress():
    return GetPickleFile(config['stress']['scalar_file'])

def GetAllClassifiersForstress():
    return (GetANNClassifier())

def GetH5File(filepath):
    """Load a TensorFlow/Keras model from a .h5 file."""
    full_path = os.path.join(dir, filepath)
    if os.path.isfile(full_path):
        return tf.keras.models.load_model(full_path)
    else:
        print(f"File does not exist: {full_path}")
        return None

def GetANNClassifier():
    """Load the ANN classifier model."""
    return GetH5File(config['stress']['ANN'])

