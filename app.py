from flask import Flask, jsonify,request
from transformers import pipeline


loaded_summarizer = pipeline("summarization", model="Falconsai/text_summarization")


app = Flask(__name__)

@app.route("/predict",methods=['POST'])
def summarize():
    max_length = request.form.get('max_length')
    text = request.form.get('text')
    try:
       result = loaded_summarizer(text, max_length=int(max_length), min_length= 10, do_sample=False)
       return jsonify({"summarized": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
 