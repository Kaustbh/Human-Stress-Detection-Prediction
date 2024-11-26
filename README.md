# Human Stress Detection and Prediction

[![Django](https://img.shields.io/badge/Django-4.x-brightgreen.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.12-blue.svg)](https://www.python.org/)

A Django-based web application that detects and predicts human stress levels during sleep using physiological data. This project employs an Artificial Neural Network (ANN) model to classify sleep data into two categories: **Stressed** or **Not Stressed**.

## 🚀 Features

- **Stress Detection**: Predicts stress levels based on input physiological data.
- **Interactive Web Interface**: User-friendly interface for uploading data and viewing results.
- **Real-Time Predictions**: Provides instant predictions based on trained ANN models.
- **Django Framework**: Built using the robust Django web framework.
- **Scalable**: Ready for deployment in real-world scenarios.


## 🛠️ Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kaustbh/Human-Stress-Detection-Prediction.git
   cd Human-Stress-Detection-Prediction

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
     ```

4. **Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Server**:
    ```bash
    python manage.py runserver
    ```

Access the application at http://127.0.0.1:8000/.

## 🔧 How It Works

1. Data Input: The user uploads physiological data (e.g., heart rate, respiration rate).

2. Model Prediction: The ANN model processes the data and predicts stress levels.

3. Results Display: The prediction result is displayed on the web interface.

## 🌐 Live Demo
[Coming Soon!]

## 🤝 Contributions
Contributions are welcome! Please follow these steps:

1. Fork this repository.

2. Create a new branch: git checkout -b feature-name.

3. Make your changes and commit them: git commit -m 'Add some feature'.

4. Push to the branch: git push origin feature-name.

5. Submit a pull request.

## 📧 Contact
For any inquiries or feedback, feel free to reach out:

- Name: Kaustubh

- Email: [desalekaustubh3@gmail.com](desalekaustubh3@gmail.com)

- GitHub: [Kaustbh](https://github.com/Kaustbh)
