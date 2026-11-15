import pandas as pd
import os

from evidently import Report
from evidently.presets import DataDriftPreset


def monitor_data():

    if not os.path.exists("division_inputs.csv"):
        print("No input data available.")
        return

    current_data = pd.read_csv("division_inputs.csv")

    if len(current_data) < 5:
        print("At least 5 API requests are required.")
        return

    # Reference dataset for comparison
    reference_data = pd.DataFrame({
        "num1": [
            10, 20, 30, 40, 50,
            60, 70, 80, 90, 100
        ],
        "num2": [
            2, 4, 5, 8, 10,
            3, 7, 9, 5, 10
        ]
    })

    # Generate Evidently data drift report
    report = Report([
        DataDriftPreset()
    ])

    result = report.run(
        current_data=current_data[["num1", "num2"]],
        reference_data=reference_data
    )

    # Save report
    result.save_html("evidently_report.html")

    print("Evidently monitoring completed.")
    print("Report saved as evidently_report.html")


if __name__ == "__main__":
    monitor_data()