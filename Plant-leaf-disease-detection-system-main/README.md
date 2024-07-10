# Plant-leaf-disease-detection-system

This project utilizes AI algorithms to detect diseases in plant leaves from images. The system leverages a trained deep learning model to classify and identify various plant diseases. A user-friendly graphical user interface (GUI) built with Tkinter allows users to easily load images and view predictions.

## Features

- **Image Classification**: Identifies diseases in plant leaf images using a pre-trained deep learning model.
- **Graphical User Interface (GUI)**: Provides an intuitive interface for selecting images and displaying predictions.
- **Confidence Scores**: Shows the confidence levels for each prediction.
- **Support for Multiple Plant Species**: Can detect diseases in various plant species, including apple, blueberry, cherry, corn, grape, orange, peach, pepper, potato, raspberry, soybean, squash, strawberry, and tomato.

## Requirements

- Python 3.x
- Keras
- TensorFlow
- NumPy
- Pillow
- Tkinter

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-leaf-disease-detection.git
   cd plant-leaf-disease-detection
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the trained model (`model.h5`) in the `model` directory.

## Usage

### Running the GUI Application

1. Start the GUI application by running the following command:
   ```bash
   python plant_leaf_detection_gui.py
   ```

2. In the application window, click "Choose Image and Detect" to select an image of a plant leaf.

3. The application will display the predicted disease along with the confidence score.

## Example Output

### GUI Example

![Screenshot (93)](https://github.com/Ajanta364/Plant-leaf-disease-detection-system/assets/174923401/7c5b0ea4-4d82-4260-b922-62c2a55539d0)


### Prediction Example

![Screenshot (95)](https://github.com/Ajanta364/Plant-leaf-disease-detection-system/assets/174923401/fae4a566-e201-4749-944b-9b937f6527a2)


![Screenshot (94)](https://github.com/Ajanta364/Plant-leaf-disease-detection-system/assets/174923401/c4d5b349-1788-4d20-8ef8-7c0daeeb1602)


## Model Details

The deep learning model used for this project is trained on a dataset of plant leaf images. It can classify the following diseases:

- Apple: Apple scab, Black rot, Cedar apple rust, Healthy
- Blueberry: Healthy
- Cherry: Powdery mildew, Healthy
- Corn (maize): Cercospora leaf spot (Gray leaf spot), Common rust, Northern Leaf Blight, Healthy
- Grape: Black rot, Esca (Black Measles), Leaf blight (Isariopsis Leaf Spot), Healthy
- Orange: Haunglongbing (Citrus greening)
- Peach: Bacterial spot, Healthy
- Pepper (bell): Bacterial spot, Healthy
- Potato: Early blight, Late blight, Healthy
- Raspberry: Healthy
- Soybean: Healthy
- Squash: Powdery mildew
- Strawberry: Leaf scorch, Healthy
- Tomato: Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites (Two-spotted spider mite), Target Spot, Tomato Yellow Leaf Curl Virus, Tomato mosaic virus, Healthy

## Acknowledgements

This project was developed as part of an internship with Next24Tech. 
