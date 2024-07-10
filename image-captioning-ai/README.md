# Image Captioning
   - Defined and trained an Image Caption Generator model on the Flickr 8K image dataset and achieved a BLEU-1 score of 0.546282 and BLEU-2 score of 0.320683.
   - Used pretrained VGG16 CNNd model for image feature extraction after removing the last classification layer.
   - Implemented Long Short-Term Memory Recurrent Neural Network layer in the model.
   - Created a web server for hosting the web application using Python Flask.
   - Created GUI using HTML, Javascript and Bootstrap.

   ## BLEU Score
   - Bilingual Evaluation Understudy scores are a metric used to evaluate the quality of text which has been machine-translated from one language to another. They are also commonly used for evaluating the quality of generated text in tasks like image captioning, where the generated text is compared against one or more reference texts.
   - BLEU-1: Measures the precision of unigrams (single words). It checks how many single words in the generated text match the reference text.
   - BLEU-2: Measures the precision of bigrams (pairs of consecutive words). It checks how many word pairs in the generated text match the reference text.
   - BLEU-1 score of 0.546282 and BLEU-2 score of 0.320683 are considered reasonably good scores. For state-of-the-art models, BLEU-1 scores can often be in the range of 0.6 to 0.7, and BLEU-2 scores can be around 0.4 to 0.5 or higher.
   
   ## Model Architecture
   ![model](https://github.com/manav-chan/AspireNex/assets/71835184/2df41241-fe5e-49b3-97ea-c8d984793c52)

   ## How to use?
   1. Clone this repository, navigate into the repository.
   2. Download the machine learning model from this [link](https://drive.google.com/file/d/1EQ1gj9u3hHrDGsxhL1C-g1-PA_lAwUnV/view?usp=sharing) into the root directory of the application.
   3. Create a python virtual environment.
      ```terminal
      python3 -m venv venv
      ```
   4. Activate the virtual environment.
      ```terminal
      source venv/bin/activate
      ```
   5. Build the project.
      ```terminal
      pip install -r requirements.txt
      ```
   6. Run the appliction.
      ```terminal
      python app.py
      ```

   ## GUI
   ![image](https://github.com/manav-chan/AspireNex/assets/71835184/1296ab46-0bf6-418e-b089-4c5569c23c06)
   ![image](https://github.com/manav-chan/AspireNex/assets/71835184/319566c8-a25c-43a7-b9eb-62cefdb0491b)

