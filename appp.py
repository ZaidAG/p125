from PIL import Image
from flask import Flask,jsonify,request
from alpha import get_prediction
app=Flask(__name__)

@app.route("/predict-alpha",methods=["POST"])
def predict_data():
    image=request.files.get("alphabet")
    prediction=get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200
if __name__ == "__main__":
    app.run(debug=True)