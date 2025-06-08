from flask import Flask, render_template, request
import urllib.request
import json
app = Flask(__name__)
api = "0f1f3e23fbbcc5c9b4c24d38e2f08a84"
url = "http://api.openweathermap.org/data/2.5/weather"


@app.route('/', methods = ['GET','POST'])


def weather():
    data = None
    error = None
    loc = request.form.get('city','ambala')


    if(request.method == 'POST'):
       
       try:
        api_url = f"{url}?q={loc}&appid={api}&units=metric"
        resp = urllib.request.urlopen(api_url)
        weather = resp.read().decode('utf-8')
        wea = json.loads(weather)


        if(wea.get('cod') != 200):
           error = f"Error: Invalid city"


        else:
         
         data = {
          "country_code": wea["sys"]["country"],
          "temp": f"{wea['main']['temp']} °C",
          "location": wea["name"],
         }


       except Exception as e:
         
        error = f'API Error Occured'
    return render_template('index2.html', error = error, data = data)


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080, debug = True)

























