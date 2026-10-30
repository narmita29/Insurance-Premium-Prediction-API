from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal,Annotated
import pickle
from config.city_tier import tier_1_cities, tier_2_cities




#pydantic model ------
class UserInput(BaseModel):
    age:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    height:Annotated[float, Field(..., gt=0, description='Height of the user in meters')]
    weight:Annotated[float, Field(..., gt=0, description='Weight of the user')]
    city:Annotated[str, Field(..., description='City of the user')]
    income_lpa:Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
    smoker:Annotated[bool, Field(..., description='Is User a smoker?')]
    occupation:Annotated[Literal['student', 'retired', 'business_owner', 'government_job',
       'freelancer', 'private_job', 'unemployed'], Field(..., description='Occupation of the user')]
    
    #now i want that city and CITY must be same so i use field_validator:

    @field_validator('city')
    @classmethod
    def normalize_city(cls, value: str) ->str:
        return value.strip().title()

    
    #BMI field
    @computed_field
    @property
    
    def BMI(self) -> float:
        return self.weight / (self.height**2)
    
    
    #lifestyle_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.BMI > 30:
            return 'High'
        elif self.smoker or self.BMI > 27:
            return 'Medium'
        else:
            return 'Low'
    
    #age group field 
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'Young'
        elif self.age < 45:
            return 'Adult'
        elif self.age < 60:
            return 'Middle_aged'

        return 'Senior'

    # City Tier field 
    @computed_field
    @property
    
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3



