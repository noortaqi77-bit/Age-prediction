# Age Prediction 


## 1. Overview
A CNN that predicts a person's age (in years) from a face image.

**Task:** regression. The model takes a 64x64 RGB face image and outputs one number, the predicted age. Quality is measured by MAE, the average error in years.



## 2. Dataset
- Source: UTKFace from Kaggle: (jangedoo/utkface-new)  with : 23,708 images.
- Images: 200x200 RGB. The age is the first number in the picture name
- Split: 17,128 train 70% and 3,023 validation and 3,557 test for each 15%
- Age distribution: a lot of images with 20 to 40 years , less than one year

## 3. Preprocessing
- Read the age from the file name (first number) as the label.
- Resize images to 64x64 and keep RGB (3 channels).
- Normalize pixels by dividing by 255.
- Split into 70% train, 15% validation, 15% test( The test set is used only for the final evaluation)

- 
 ## 4. Model Architecture
Conv2D(20) → MaxPooling → Conv2D(30)  → MaxPooling →  Conv2D(40) → Flatten → Dense(100) x3 → Dense(1)

Loss: MAE. Metric: MAE. Optimizer: Adam. EarlyStopping by patience=3

## 5. Training and Improvement
- **First model (default learning rate):** validation MAE about 6.6. The model overfit: training MAE fell to about 5.2 and kept falling while validation MAE stayed around 6.6-6.9.
- **Improvement 1 (lower learning rate):** Adam with learning rate 1e-4. Test MAE improved from 6.51 to 6.18.

## 6. Error Analysis
Images with an error above 5 years were inspected. Main causes:
- **Older people and children:** the dataset has fewer images for these ages, so errors are larger.
- **Makeup, glasses and lighting:** they hide or change age cues such as wrinkles and skin texture.

## 7. App (Gradio)
The app take uploaded face image or webcam photo and shows the predicted age in years

link= ()

## 10. Ethics & Limitations
- Accuracy drops with poor lighting, tilted faces, makeup and low resolution.
- Age estimation is hard even for humans, so predictions are approximate (error of about 6 years).
- UTKFace is not balanced across ages and ethnicities, so results may be biased.
