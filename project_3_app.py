import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the model and scaler
model = RandomForestClassifier(n_estimators=100, random_state=42)
cleaned_file_path = 'cleaned_cardio_train.csv'
data = pd.read_csv(cleaned_file_path)

# Select the first 6 features for the model
selected_features = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol']
X = data[selected_features]
y = data['cardio']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
model.fit(X_train_scaled, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    final_features_scaled = scaler.transform(final_features)
    prediction = model.predict(final_features_scaled)
    
    output = "You have a high risk of cardiovascular disease" if prediction[0] == 1 else "You have a low risk of cardiovascular disease"
    
    return render_template('results.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
