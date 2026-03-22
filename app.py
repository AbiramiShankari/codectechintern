from flask import Flask, render_template, request
import os
from model import predict_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    label = None
    confidence = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            label, confidence = predict_image(filepath)

    return render_template('index.html', label=label, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
