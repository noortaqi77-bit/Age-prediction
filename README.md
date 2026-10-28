# Age Prediction 


## 1. Overview
A CNN that predicts a person's age (in years) from a face image.
**Task:** regression. The model takes a 64x64 RGB face image and outputs one number, the predicted age. Quality is measured by MAE, the average error in years.



## 2. Dataset
- Source: UTKFace (Kaggle: jangedoo/utkface-new), 23,708 images.
- Images: 200x200 RGB. The age is the first number in the file name.
- Split: 17,128 train | 3,023 validation | 3,557 test
- Age distribution

## 3. Preprocessing
- Read the age from the file name (first number) as the label.
- Resize images to 64x64 and keep RGB (3 channels).
- Normalize pixels by dividing by 255.
- Split into 70% train, 15% validation, 15% test (`random_state=42`). The test set is used only for the final evaluation.

- 
 ## 4. Model Architecture
Conv2D(20) → MaxPooling → Conv2D(30) → MaxPooling → Conv2D(40) → Flatten → Dense(100) x3 → Dense(1)
Loss: MAE. Metric: MAE. Optimizer: Adam. EarlyStopping (patience=3, restore_best_weights=True).

- 
