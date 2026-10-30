#a response model defines the expected structure of the APIs output using a pudantic structure.(validates wht your API sends back to user)
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_category: str=Field(..., description='Predicted Insurance premium category',
    examples=['High']
    )

    confidence:float=Field(..., description='confidence score of the prediction',
    examples=[0.85])

    class_probabilities:dict[str,float]=Field(...,
     description='probability for each premium category',
     examples=[
        {
            'High':0.85,
            'Medium':0.10,
            'Low':0.5
        }])


