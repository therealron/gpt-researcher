from fastapi import FastAPI
from pydantic import BaseModel

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


@app.post("/generate_report/")
async def create_report(query: QueryItem):
    print(query)
    return item

@app.post("/")
async def root():
    return {"message": "Hello World"}