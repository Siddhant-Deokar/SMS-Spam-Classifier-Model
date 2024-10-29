# SMS Spam Classification

**This project implements a Logistic Regression model that classifies text messages as Spam or Not Spam.**

## Features

- Built using Python and Streamlit for an interactive web interface.
- Utilizes TF-IDF vectorization for text processing.
- Scales features using MinMaxScaler for better model performance.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage
* After launching the application, you will see an input box where you can enter a text message.
* Click the "Predict" button to determine whether the message is classified as Spam or Not Spam.
* The result('Spam' or 'Not Spam') will be displayed on the screen
