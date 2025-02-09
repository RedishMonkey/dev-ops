from flask import Flask, request

app = Flask(__name__)

# Log all requests and responses to a file
LOG_FILE = "logs.txt"

def log_request_response(req_data, res_data):
    with open(LOG_FILE, "a") as log:
        log.write(f"Request: {req_data}\n")
        log.write(f"Response: {res_data}\n")
        log.write("="*50 + "\n")

@app.route("/", methods=["GET", "POST"])
def log_requests():
    req_data = f"{request.method} {request.url} - Data: {request.data.decode('utf-8')}"
    res_data = "Logged Successfully"
    log_request_response(req_data, res_data)
    return res_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
