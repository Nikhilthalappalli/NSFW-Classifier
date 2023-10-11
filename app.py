import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.image as mpimg

# Load the pre-trained model
def setup_model():
    path = 'vgg16.h5'  # Replace with the path to your model
    model = tf.keras.models.load_model(path)
    return model

# Predict the class of the image
def predict_class(image):
    model = setup_model()
    classes = ['Drawing', 'Hentai', 'Neutral', 'Porn', 'Sexual']
    img = mpimg.imread(image)
    resize = tf.image.resize(img, (224, 224))
    result = model.predict(np.expand_dims(resize / 255, 0))
    result = np.argmax(result)
    if result in [1, 3, 4]:
        m = 1
    else:
        m = 0
    return classes[result], m

# Main Streamlit app
def main():
    st.title("Image Classifier App")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        result, m = predict_class(uploaded_image)
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        st.write("Result:", result)
        st.write("Is Explicit (1) or Not (0):", m)

if __name__ == "__main__":
    main()
