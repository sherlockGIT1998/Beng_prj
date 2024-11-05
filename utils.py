import pickle 
import json 
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import config 

class BengaluruHousePrice():
    
    def __init__(self,area_type,availability,location,size,total_sqft,bath,balcony):
        
        self.availability = availability
        self.location = location
        self.total_sqft = total_sqft
        self.bath = bath 
        self.balcony = balcony
        
        self.area_type_col = 'area_type_'+area_type
        
        self.size_col = 'size_'+size
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_price(self):
        
        self.load_models()
        
        area_type_col_index = np.where(self.column_names==self.area_type_col)[0]
        
        size_col_index = np.where(self.column_names==self.size_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.save_data['availability'][self.availability]
        array[1] = self.save_data['location'][self.location]
        array[2] = self.total_sqft
        array[3] = self.bath
        array[4] = self.balcony

        array[area_type_col_index] == 1
        array[size_col_index] == 1
        print('Array is :',array)
        
        price = self.model.predict([array])[0]
        
        return price 
    
if __name__ == '__main__':
    
    availability = '19-Dec'
    location = 'Electronic City Phase II'
    total_sqft = '1056.0'
    bath = 2.0
    balcony = 1.0

    area_type = 'Built-up Area'

    size = '1 BHK'
    
    house_price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
    
    price = house_price.get_predicted_price()
    
    print('Price of Bengaluru House is : Rs. ',round(price,2),'Lakh/-')
    print(f'Price of Bengaluru House is : Rs. {round(price,2)} Lakh/-')
            