from pickle import TRUE
from flask import Flask, request, render_template, redirect, make_response, jsonify

# init Flask
app = Flask(__name__)


@app.route("/", methods = ["GET"])
def main():
	return render_template("chatbot.html"), 200


if __name__ == '__main__':
    app.run(debug = TRUE, host = '0.0.0.0', port = 3000)

