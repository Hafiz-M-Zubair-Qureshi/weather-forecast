from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests


app=FastAPI()

url="https://freetestapi.com/api/v1/weathers"

data=requests.get(url)
my_data=data
weather=my_data.json()
my_weather=weather


templates=Jinja2Templates(directory="templates")

@app.get("/all_weathers/")
async def all_weather(request:Request):
    context={"request":request,"weathers":my_weather}
    return templates.TemplateResponse("allcities.html",context)

@app.get("/cities/{weather_id}")
async def read_weather(request:Request,weather_id:int):
    for weather in my_weather:
        if weather ["id"]==weather_id:
            context={"request":request,"weather":weather}
            return templates.TemplateResponse("cities.html",context)



