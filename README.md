# Sign Language Detector

This project utilizes computer vision and machine learning to detect and classify sign language gestures in real-time. The system leverages **MediaPipe** for hand landmark detection and **scikit-learn** for classification.

## Project Overview

This application recognizes hand gestures corresponding to the **26 letters of the American Sign Language (ASL) alphabet** using a webcam. The system extracts hand landmark features and employs a **Random Forest classifier** to predict the corresponding letter.

## Features

- 🎥 **Real-time hand gesture recognition**
- 🔠 **Support for all 26 ASL alphabet letters**
- 📈 **99.6% classification accuracy**
- 👀 **Visual feedback with landmark visualization**
- 🖥️ **Easy-to-use interface**

## Prerequisites

- **Python** 3.8 or higher
- **Webcam**
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**git reset --hard origin/master

   ```sh
   git clone https://github.com/Yuldy/sign-language-detector-python
   cd sign-language-detector-python
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Project Structure

```
sign-language-detection/
├── collect_imgs.py           # Collect hand gesture images
├── create_dataset.py         # Process images and extract features
├── train_classifier.py       # Train the Random Forest model
├── inference_classifier.py   # Real-time sign language detection
├── requirements.txt          # Required dependencies
├── data/                     # Collected image data
│   ├── 0/                    # Images for specific gestures
│   ├── 1/
│   ├── 2/
│   └── ...
└── models/                   # Trained models
    └── random_forest_model.pkl  # Trained classifier
```

## Usage

### 1️⃣ Data Collection

If you want to collect your own dataset (skip if using pre-existing data):

```sh
python collect_imgs.py
```

Follow the on-screen prompts to capture images for each gesture. Press **'q'** to stop collecting images for a gesture.

### 2️⃣ Creating the Dataset

Process the collected images and extract hand landmark features:

```sh
python create_dataset.py
```

This will generate a structured dataset for training.

### 3️⃣ Training the Classifier

Train the Random Forest classifier:

```sh
python train_classifier.py
```

The trained model will be saved in the `models/` directory.

### 4️⃣ Real-time Inference

Run real-time sign language detection:

```sh
python inference_classifier.py
```

Make hand gestures in front of your webcam and see the detected letters displayed in real time.

## Technical Implementation

- **Hand Detection:** MediaPipe extracts **21 key landmarks** from each hand.
- **Feature Extraction:** Each landmark provides **x** and **y** coordinates, yielding **42 features** per gesture.
- **Model:** Random Forest classifier with optimized hyperparameters.
- **Preprocessing:** Landmark coordinates are normalized for position-invariant features.

## Performance

- ✅ **99.6% accuracy** on the test dataset
- 🚀 **Real-time inference at ~30 FPS** (depends on hardware)
- 🖐️ **Robust to variations in hand size and positioning**

## Requirements

All dependencies are listed in `requirements.txt`:

```
opencv-python==4.7.0.68
mediapipe==0.9.0.1
scikit-learn==1.2.0
numpy>=1.20.0
matplotlib>=3.5.0
```

## Troubleshooting

| Issue                   | Solution |
|-------------------------|----------|
| ❌ No webcam detected  | Ensure your webcam is connected and not used by another app. |
| 🤏 Poor recognition accuracy | Adjust lighting and ensure your hand is fully visible. |
| 📂 Model not found | Run `train_classifier.py` before inference. |



## Acknowledgments

- Hand landmark detection powered by **MediaPipe**
- Classification powered by **scikit-learn**
