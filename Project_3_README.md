# Cardiovascular Disease Prediction System

This project is a web application that predicts the likelihood of a user having cardiovascular disease based on their health data. It uses a Random Forest classifier trained on a cleaned dataset of health records.

## Project Structure

- `index.html`: The main page where users input their health data.
- `results.html`: The results page that displays the prediction.
- `app.py`: The Flask application script that handles user input and prediction logic.
- `cleaned_cardio_train.csv`: The dataset used to train the machine learning model.

## How to Run the Project

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-learn

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/DiseasePredictionSystem.git
   cd DiseasePredictionSystem
   ```

2. **Install the Required Libraries**

   Install the required Python libraries using pip:

   ```bash
   pip install flask pandas scikit-learn
   ```

3. **Run the Flask Application**

   Start the Flask application by running:

   ```bash
   python app.py
   ```

4. **Access the Application**

   Open a web browser and navigate to `http://127.0.0.1:5000/`. You will see the Cardiovascular Disease Predictor form.

5. **Use the Application**

   - Input your health data (age, height, weight, systolic blood pressure, diastolic blood pressure, and cholesterol level) and submit the form.
   - The prediction result will be displayed on the results page.

## Dataset

The dataset used in this project (`cleaned_cardio_train.csv`) contains the following features:
- `age`: Age of the patient
- `height`: Height of the patient in cm
- `weight`: Weight of the patient in kg
- `ap_hi`: Systolic blood pressure
- `ap_lo`: Diastolic blood pressure
- `cholesterol`: Cholesterol level (1: normal, 2: above normal, 3: well above normal)
- `cardio`: Cardiovascular disease indicator (1: presence, 0: absence)

## Model

The machine learning model used is a Random Forest classifier. The model is trained on the provided dataset and predicts the likelihood of cardiovascular disease based on the input features.

## Notes

- Ensure that `cleaned_cardio_train.csv` is in the same directory as `app.py`.
- Modify the dataset path in `app.py` if your dataset is located elsewhere.

