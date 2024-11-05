from flask import Flask,render_template,request

from utils import BengaluruHousePrice

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Bengaluru House Price Prediction...')
    return render_template('index.html')

@app.route('/predict_prices',methods=['GET','POST'])
def price_info():
    if request.method == 'GET':
        print('In GET Method...')
        
        data = request.form
        area_type = data['area_type']
        availability = data['availability']
        size = data['size']
        location = data['location']
        bath = eval(data['bath'])
        balcony = eval(data['balcony'])
        total_sqft = data['total_sqft']
        
        house_price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
        
        price = house_price.get_predicted_price()
        
        return f'Price of Bengaluru House is : Rs. {round(price,2)} Lakh/-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()