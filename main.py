from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Request, Response
from typing import Any

app = FastAPI(root_path="/api/v1")

data = [
    {
        "campaign_id" : 1,
        "name" : "Black Friday",
        "due_date" : datetime.now(),
        "created_at" : datetime.now()
    },

    {
        "campaign_id" : 2,
        "name" : "TechnoVIT",
        "due_date" : datetime.now(),
        "created_at" : datetime.now()        
    }
]

@app.get("/")
async def root():
    return {"message" : "Hello World!"}

@app.get("/campaign")
async def campaign():
    return data

@app.get("/campaign/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return campaign
    raise HTTPException(status_code = 404)

@app.post("/campaign", status_code=201)
async def create_campaign(body : dict[str, Any]):
    
    new = {
        "campaign_id" : randint(100,1000),
        "name" : body.get("name"),
        "due_date" : body.get("due_date"),
        "created_at" : datetime.now()
    }
    data.append(new)
    return {"campaign" : data}

@app.put("/campaign/{id}")
async def update_campaign(id : int,body: dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            new : Any = {
                "campaign_id" : id,
                "name" : body.get("name"),
                "due_date" : body.get("due_date"),
                "created_at" : campaign.get("created_at")
            }
            data[index] = new
            return new
    
    raise HTTPException(status_code=404, detail="campaign not found")



@app.delete("/campaign/{id}")
async def update_campaign(id : int):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return Response(status_code = 204)
    
    raise HTTPException(status_code=404, detail="campaign not found")