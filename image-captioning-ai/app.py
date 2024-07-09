from flask import Flask, request, jsonify, send_from_directory
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np
import pickle
import os

app = Flask(__name__)
model = load_model("model.keras")
# Load the trained model
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

max_length = 35

# Load ResNet50 model for feature extraction
vgg_model = VGG16() 
# restructure the model
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

if not os.path.exists('uploads/'):
    os.makedirs('uploads/')

def extract_features(img_path):
    image = load_img(img_path, target_size=(224, 224))
    # convert image pixels to numpy array
    image = img_to_array(image)
    # reshape data for model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # preprocess image from vgg
    image = preprocess_input(image)
    # extract features
    feature = vgg_model.predict(image, verbose=0)
    return feature

def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def predict_caption(file_path):
    image = extract_features(file_path)
    # add start tag for generation process
    in_text = 'startseq'
    # iterate over the max length of sequence
    for i in range(max_length):
        # encode input sequence
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        # pad the sequence
        sequence = pad_sequences([sequence], max_length)
        # predict next word
        yhat = model.predict([image, sequence], verbose=0)
        # get index with high probability
        yhat = np.argmax(yhat)
        # convert index to word
        word = idx_to_word(yhat, tokenizer)
        # stop if word not found
        if word is None:
            break
        # append word as input for generating next word
        in_text += " " + word
        # stop if we reach end tag
        if word == 'endseq':
            break
    in_text = in_text[len('startseq'):]
    in_text = in_text[:-len('endseq')].strip()
    in_text += '.'
    return in_text.capitalize()

@app.route('/')
def index():
    return send_from_directory('', 'index.html')


@app.route('/caption', methods=['POST'])
def caption_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        file_path = os.path.join('uploads/', file.filename)
        file.save(file_path)
        try:
            caption = predict_caption(file_path)
        finally:
            os.remove(file_path)
        return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(debug=True)
