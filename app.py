from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>On-Prem Kubernetes</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    background-color: #f0f8ff;
                }
                h1 { 
                    color: #4682B4; 
                    margin-top: 20%;
                }
                p { 
                    font-size: 20px; 
                    color: #555; 
                }
            </style>
        </head>
        <body>
            <h1>This Python Application is Running on On-Prem Kubernetes</h1>
            <p>Powered by your home lab!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
