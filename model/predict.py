import pandas as pd
import pickle
#import ml model
import pickle
with open('model/model.pkl', 'rb') as f:  # model folder ka under

    model = pickle.load(f)

Model_Version='1.0.0'

class_labels= model.classes_.tolist()  #we will get a list of our output



def predict_output(User_Input):
    df=pd.DataFrame([User_Input])

    print('DataFrame shape:', df.shape)
    print(df)
    #predict the class

    predicted_class = model.predict(df)[0]
    probabilities=model.predict_proba(df)[0]
    class_probs = dict(
        zip(class_labels, map(lambda p: round(p,4), probabilities))
        )# zip() pair each class with its rounded probability Dict converts those pair into dict lambda p: round(p, 4) defines the rounding operation.map() applies that operation to every probability.

    confidence = max(probabilities)    #selects the largest value of cofidence
    
    
    return{
        'predicted_category': predicted_class,
        'confidence': round(confidence,4),
        'class_probabilities': class_probs
    }

