import json
from fastapi.routing import APIRouter
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# router = APIRouter(prefix="")
# app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/research_info")
async def get_research_info():
    file = open('be/example.json')
    json_result = json.load(file)

    year_graph = []
    for row in json_result["cited_by"]["graph"]:
        year_graph.append([row["year"], row["citations"]])

    structure = {
        "number_of_articles": len(json_result["articles"]),
        "number_of_citations": json_result["cited_by"]["table"][0]["citations"]["all"],
        "h_index": json_result["cited_by"]["table"][1]["h_index"]["all"],
        "year_graph": year_graph,
    }
    return structure

if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=5000,
        log_level="info",
        reload=True,
        reload_excludes="storage",
    )