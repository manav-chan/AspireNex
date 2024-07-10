from flask import Flask, request, jsonify, send_from_directory
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np
import pickle
import os

app = Flask(__name__)
model = load_model("model.keras")

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# max length for caption (for padding)
max_length = 35

# VGG16 model for feature extraction
vgg_model = VGG16() 
# restructuring the model to extract features
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

if not os.path.exists('uploads/'):
    os.makedirs('uploads/')

def extract_features(img_path):
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    feature = vgg_model.predict(image, verbose=0)
    return feature

def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def predict_caption(file_path):
    image = extract_features(file_path)
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], max_length)
        yhat = model.predict([image, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idx_to_word(yhat, tokenizer)
        if word is None:
            break
        in_text += " " + word
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


