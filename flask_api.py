from flask import Flask
from query_services import *
from report import report

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index":True}

@app.route("/show_shifts/", methods=["GET"])
def get_shift_table():
    try:
        return show_shifts()
    except:
        return {"error": "no data"}

@app.route("/report", methods=["GET"])
def trigger_report():
    try:
        report() 
        return {"success": "Report generated and uploaded to Azure Blob Storage"}
    except Exception as e:
        return {"error": str(e)}

# http://127.0.0.1:5000/show_shifts
# http://127.0.0.1:5000/report

if __name__ == "__main__":
    app.run()