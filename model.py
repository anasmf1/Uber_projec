import pickle

# Replace 'path/to/model.pkl' with the actual path to your .pkl file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Display information about the model
print("Model loaded successfully!")
print(model)
