from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os

app = FastAPI(title="Division Calculator API")


class DivisionInput(BaseModel):
    num1: float
    num2: float


@app.get("/")
def home():
    return {"message": "Welcome to Division Calculator API"}


@app.post("/divide")
def divide(data: DivisionInput):

    if data.num2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )

    result = data.num1 / data.num2

    # Store input data for Evidently monitoring
    file_exists = os.path.isfile("division_inputs.csv")

    with open("division_inputs.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["num1", "num2"])

        writer.writerow([data.num1, data.num2])

    return {
        "num1": data.num1,
        "num2": data.num2,
        "result": result
    }