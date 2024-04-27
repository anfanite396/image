from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Hello, World!</title>
        <script>
            function printMessage() {
                document.getElementById("message").innerText = "Good job";
            }
        </script>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <button onclick="printMessage()">Click me</button>
        <p id="message"></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
