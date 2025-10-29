from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load your trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = vectorizer.transform(data).toarray()
        prediction = model.predict(vect)[0]

        if prediction == 1:
            result = "🚨 Spam Message Detected!"
        else:
            result = "✅ Not a Spam Message."

        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
