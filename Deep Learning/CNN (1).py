import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout


st.set_page_config(
    page_title="Dog vs Cat Classifier",
    page_icon="🐶🐱",
    layout="centered"
)

st.title("🐶🐱 Dog vs Cat Image Classifier")
st.write("Upload an image and classify it as Dog or Cat.")

IMG_SIZE = 128


def create_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        MaxPooling2D(2,2),
        Dropout(0.25),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Dropout(0.25),

        Conv2D(128, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Dropout(0.25),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(2, activation='softmax')
    ])

    return model


@st.cache_resource
def load_model():

    model = create_model()


    try:
        model = tf.keras.models.load_model("dogcat_model.keras")
        return model
    except:
        pass


    try:
        model.load_weights("model.h5")
        return model
    except:
        st.error("❌ No valid model found.")
        st.info("Run notebook and save model using:")
        st.code('model.save("dogcat_model.keras")')
        st.stop()

model = load_model()

uploaded_file = st.file_uploader(
    "Upload Cat / Dog Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    if st.button("Predict"):

        pred = model.predict(img)
        class_id = np.argmax(pred)
        confidence = np.max(pred)

        if class_id == 0:
            st.success("🐱 Prediction: Cat")
        else:
            st.success("🐶 Prediction: Dog")

        st.info(f"Confidence: {confidence:.2%}")


st.sidebar.title("Notebook Model")
st.sidebar.write("""
Architecture loaded from your notebook:

✔ Conv2D(32)  
✔ Conv2D(64)  
✔ Conv2D(128)  
✔ Dense(128)  
✔ Softmax Output
""")