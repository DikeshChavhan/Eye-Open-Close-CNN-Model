# 👁️ Eye Open / Closed Detection using CNN & Streamlit

🔗 **Live App:** https://eye-open-close-cnn-model.streamlit.app/

A Computer Vision project that detects whether a human eye is **Open or Closed** using a Convolutional Neural Network (CNN).  
The model is trained in **Google Colab** using the **MRL Eye Dataset** and deployed as a **Streamlit Web Application**.

---

## 🚀 Features

- Image-based Eye State Classification (Open / Closed)
- CNN model built using **TensorFlow / Keras**
- Image preprocessing with **OpenCV**
- Lightweight & fast prediction pipeline
- Simple browser-based UI using **Streamlit**

---

## 🧠 Tech Stack

- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Streamlit  

---

## 📂 Project Structure
eye-open-close-app/
│
├── app.py # Streamlit application
├── eye_open_close_cnn.h5 # Trained CNN model
├── requirements.txt # Dependencies
└── README.md

---

## 🏗️ Model Training (Colab)

The model was trained using:

- ImageDataGenerator with augmentation  
- Binary classification (Open = 1, Closed = 0)  
- 64×64 RGB images  
- CNN architecture with Conv-Pooling layers + Dropout  

The trained model was exported as: eye_open_close_cnn.h5

---

## 💻 Run the Project Locally

### 1️⃣ Install dependencies

pip install -r requirements.txt

graphql
Copy code

### 2️⃣ Run the Streamlit app

streamlit run app.py

yaml
Copy code

### 3️⃣ Upload an eye image → View Prediction 🎯

---

## 🌐 Deployment (Streamlit Cloud)

This project is deployed on **Streamlit Community Cloud** by connecting the GitHub repository and selecting `app.py` as the entry file.

---

## 📊 Future Improvements

- Add real-time webcam eye detection  
- Integrate face detection + drowsiness monitoring  
- Improve dataset balance & accuracy  
- Convert model to **TFLite** for faster loading  

---

## 🧑‍💻 Author

**Dikesh Chavhan**  
Machine Learning & Computer Vision Enthusiast

---


