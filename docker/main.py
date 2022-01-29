# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

@app.get("/")
async def root():
    """Return welcome message at root address, point users to API documentation."""
    return """Welcome to the API Demo, go to localhost:8000/docs to veiw API documentation""" 
    

@app.get("/ad_buy/", response_class=HTMLResponse)
async def predict_units_sold(tv_buy:int,radio_buy:int):
    """Takes URL based query parameters and uses those to predict units sold based on tv ad spend and radio ad spend.
    
    Input Variables: tv_buy (int)
                     radio_buy (int)
                     
    Format: http://localhost:8000/ad_buy/?tv_buy={int}&radio_buy={int}
    
    Example: http://localhost:8000/ad_buy/?tv_buy=400&radio_buy=200
    """
    model = pickle.load( open( "ad_model", "rb" ))
    predicted_units_sold = model.predict([[tv_buy, radio_buy]])
    return_string = "Predicted units sales : " + str(predicted_units_sold[0]) + "<br>"\
           + " When your spend on TV is : " + str(tv_buy) + "<br>"\
           + " And your spend on Radio is : " + str(radio_buy)
    return return_string
    