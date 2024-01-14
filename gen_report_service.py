from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from gpt_researcher import GPTResearcher
import asyncio


async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report


class QueryItem(BaseModel):
    query: str
    # description: str | None = None
    # price: float
    # tax: float | None = None


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/generate_report/")
async def create_report(query: QueryItem):
    print(query)
    return item

@app.get("/")
async def read_root():
    return {"Hello": "World"}
