# plant_leaf_detection_gui.py

from tkinter import Tk, Label, Button, filedialog, Canvas
from PIL import Image, ImageTk
from detection import initialize_model_and_labels, predict_image

class PlantDiseaseDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plant Leaf Disease Detection")
        self.root.geometry("600x600")

        self.label = Label(root, text="Plant Leaf Disease Detection System", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.detect_button = Button(root, text="Choose Image and Detect", command=self.load_and_predict)
        self.detect_button.pack(pady=10)

        self.result_label = Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.canvas = Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.initialize_model_and_labels()

    def initialize_model_and_labels(self):
        initialize_model_and_labels()

    def load_and_predict(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            predicted_label, prediction = predict_image(file_path)
            self.result_label.config(text=f"Prediction: {predicted_label}\nConfidence: {max(prediction[0]):.2f}")

            # Load and display the image
            img = Image.open(file_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.canvas.create_image(150, 150, anchor='center', image=img)
            self.canvas.image = img

def main():
    root = Tk()
    app = PlantDiseaseDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
