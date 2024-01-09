from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    data = {"message": "Hello, World!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
