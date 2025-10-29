# AI Spam Email Detection

## Project Title
AI Spam Email Detection

## Description
This project implements a simple web application for detecting spam email messages using a pre-trained machine learning model. Users can input an email message into a text area, and the application will predict whether the message is spam or not, displaying the result on the same page. The backend is built with Flask, and the machine learning components (model and text vectorizer) are loaded using Python's `pickle` module.

**Key Features:**
*   **Interactive Web Interface:** A user-friendly web form to input email messages.
*   **Real-time Prediction:** Instantly classifies messages as "Spam" or "Not Spam" upon submission.
*   **Pre-trained ML Model:** Utilizes a `Multinomial Naive Bayes` classifier and a `CountVectorizer` for text processing, pre-trained on a dataset of email messages.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository (or download the project files):**
    ```bash
    git clone <repository_url>
    cd spam-email-detection
    ```
    *(Note: Replace `<repository_url>` with the actual URL if this project were hosted on GitHub.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install Flask scikit-learn
    ```

## Usage

Once the installation is complete, you can run the Flask application:

1.  **Start the Flask development server:**
    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000`.

2.  **Open your web browser** and navigate to the address displayed in your terminal (e.g., `http://127.00.1:5000`).

3.  **Enter an email message** into the provided text area on the web page and click the "Analyze" button to see the prediction.

### API Endpoints

The application exposes the following main endpoints:

*   **`GET /`**:
    *   Renders the main `index.html` page, which contains the form for message input and displays prediction results.
*   **`POST /predict`**:
    *   Accepts a form submission with a `message` field (the email content).
    *   Processes the input using the loaded `vectorizer` and `model`.
    *   Returns the `index.html` page with the prediction result (`"🚨 Spam Message Detected!"` or `"✅ Not a Spam Message."`) displayed.

## Project Structure

```
spam email detection/
├── app.py                  # Main Flask application logic
├── model.pkl               # Pre-trained machine learning model (Multinomial Naive Bayes)
├── vectorizer.pkl          # Pre-trained text vectorizer (CountVectorizer)
├── style.css               # (Unused) CSS file for potential future styling
└── templates/
    └── index.html          # HTML template for the web interface (includes inline CSS)
```

*   **`app.py`**: This is the core of the Flask application. It initializes the Flask app, loads the pre-trained model and vectorizer, defines the routes for the home page and prediction, and handles the logic for classifying messages.
*   **`model.pkl`**: A serialized Python object containing the trained `sklearn.naive_bayes.MultinomialNB` classifier. This file is loaded at application startup to make predictions.
*   **`vectorizer.pkl`**: A serialized Python object containing the trained `sklearn.feature_extraction.text.CountVectorizer`. This is used to transform raw text input into a numerical feature vector that the model can understand.
*   **`style.css`**: A CSS file containing styling rules. *Note: Currently, the `index.html` file uses inline CSS and does not link to this external stylesheet.*
*   **`templates/index.html`**: The HTML template that provides the user interface for the spam detection tool. It includes a form for text input and a section to display the prediction result.

## Technologies Used

*   **Python**: The primary programming language.
*   **Flask**: A lightweight Python web framework used for building the web application.
*   **Scikit-learn**: A machine learning library used for the `Multinomial Naive Bayes` classifier and `CountVectorizer`. The pre-trained model and vectorizer are serialized from this library.
*   **HTML5**: For structuring the web content.
*   **CSS3**: For styling the web interface (inline within `index.html`).

## Scripts

The main script to run the application is `app.py`. There are no other specific build or utility scripts provided.

To run the application:
```bash
python app.py
```

## Configuration

*   **Debug Mode**: The Flask application runs in debug mode (`app.run(debug=True)`) by default, which provides helpful error messages and automatically reloads the server on code changes. For production environments, `debug=False` should be set.
*   **Model and Vectorizer Files**: The application expects `model.pkl` and `vectorizer.pkl` to be present in the same directory as `app.py`. These files contain the pre-trained machine learning components.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## License
No specific license file was provided with this project.