from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()


@app.get('/')
async def index():
   return {"FIO": "Titova V E"}


@app.get('/users')
async def get_users():
   users = {"phone number": "8-983-177-89-74",
            "email": "123@gmail.com"}


   json_data = jsonable_encoder(users)
   return JSONResponse(content=json_data)


@app.get('/tools')
async def get_tools():
   tools = ["Python", "JS", "HTML", "CSS", "React", "Next.js"]
   json_data = jsonable_encoder(tools)
   return JSONResponse(content=json_data)