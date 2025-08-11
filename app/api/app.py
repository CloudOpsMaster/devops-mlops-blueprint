from flask import Flask, request, jsonify
import joblib, os

app = Flask(__name__)
MODEL_PATH = os.environ.get('MODEL_PATH', 'results/model.joblib')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    if not payload or 'input' not in payload:
        return jsonify({'error': 'invalid payload'}), 400
    model = joblib.load(MODEL_PATH)
    inp = [payload['input']]
    pred = model.predict(inp).tolist()
    return jsonify({'prediction': pred})
