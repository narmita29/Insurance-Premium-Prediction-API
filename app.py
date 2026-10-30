from fastapi import FastAPI
import pandas as pd
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model, Model_Version
from schema.prediction_response import PredictionResponse

app= FastAPI()


@app.get('/')
def home():
    return{'message':'Insurance Premium Category API'}


#status of our API
@app.get('/health')
def health_status():
    return{'status':'OK',
            'version':Model_Version,
            'model_loaded': model is not None
    
    }    

@app.post('/predict',response_model= PredictionResponse)

def predict_premium(data: UserInput):
#we converting the user s input into pandas datafram because our trained ml model expects data in a tabular format so we send the input in that format for prediction
    
    print('Endpoint reached')
    User_Input={
        'BMI': data.BMI,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
    }


    try:
        prediction=predict_output(User_Input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


