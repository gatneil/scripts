from flask import Flask
app = Flask(__name__)

@app.route("/checkin/<vm_id>")
def hello():
    return vm_id

    if __name__ == "__main__":
            app.run()
