from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Keep soc_model.pkl in the same directory as this Python file.
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "soc_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError as exc:
    raise FileNotFoundError(
        f"Trained model not found: {MODEL_PATH}. "
        "Export your fitted pipeline from the notebook as 'soc_model.pkl'."
    ) from exc


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Keep the entered values in the form if validation fails.
    values = {
        "temperature": request.form.get("temperature", "").strip(),
        "voltage": request.form.get("voltage", "").strip(),
        "current": request.form.get("current", "").strip(),
    }

    try:
        temperature = float(values["temperature"])
        voltage = float(values["voltage"])
        current = float(values["current"])

        if not all(np.isfinite(v) for v in (temperature, voltage, current)):
            raise ValueError

        # The order and names must match the model's training features.
        input_data = pd.DataFrame(
            [[temperature, voltage, current]],
            columns=["temp_C", "voltage_V", "current_A"],
        )

        predicted_soc = float(model.predict(input_data)[0])

        # The notebook target is a fraction (e.g. 0.75), not a percentage.
        soc_percent = predicted_soc * 100

        return render_template(
            "index.html",
            values=values,
            soc_percent=soc_percent,
        )

    except (TypeError, ValueError):
        return render_template(
            "index.html",
            values=values,
            error="Please enter valid numerical values for all three measurements.",
        )
    except Exception:
        app.logger.exception("SOC prediction failed")
        return render_template(
            "index.html",
            values=values,
            error="The SOC estimate could not be calculated. Please check the model file.",
        )


if __name__ == "__main__":
    # Local development only. Do not enable debug mode on a public deployment.
    app.run(host="127.0.0.1", port=5000, debug=False)
