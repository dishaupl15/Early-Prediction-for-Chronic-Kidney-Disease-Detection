from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("Flask/CKD.pkl", "rb"))  # Make sure this path is correct

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Collect data from form
            age = float(request.form["age"])
            bp = float(request.form["bp"])
            sg = float(request.form["sg"])
            al = float(request.form["al"])
            su = float(request.form["su"])
            rbc = float(request.form["rbc"])
            pc = float(request.form["pc"])
            pcc = float(request.form["pcc"])
            ba = float(request.form["ba"])
            bgr = float(request.form["bgr"])
            bu = float(request.form["bu"])
            sc = float(request.form["sc"])
            sod = float(request.form["sod"])
            pot = float(request.form["pot"])
            hemo = float(request.form["hemo"])
            pcv = float(request.form["pcv"])
            wc = float(request.form["wc"])
            rc = float(request.form["rc"])
            htn = float(request.form["htn"])
            dm = float(request.form["dm"])
            cad = float(request.form["cad"])
            appet = float(request.form["appet"])
            pe = float(request.form["pe"])
            ane = float(request.form["ane"])

            # Convert to NumPy array
            features = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu,
                                  sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad,
                                  appet, pe, ane]])

            prediction = model.predict(features)[0]
            result = "CKD Detected" if prediction == 1 else "No CKD"
            return render_template("predict.html", prediction_text=result)
        except:
            return render_template("predict.html", prediction_text="Invalid input. Please enter valid values.")
    
    return render_template("predict.html", prediction_text="")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
