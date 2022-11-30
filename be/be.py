import json
from textwrap import dedent
from serpapi import GoogleSearch

params = {
    "engine": "google_scholar_author",
    "author_id": "QJDxRrsAAAAJ",
    "api_key": "33de3e279cde282b3bc0de7dc4a456c9f5230dfc9e82db6a5ee105cfb3fe81da"
}




if __name__ == "__main__":
    search = GoogleSearch(params)
    json_result = search.get_dict()


    # file = open('be/example.json')
    # json_result = json.load(file)

    year_graph = []
    for row in json_result["cited_by"]["graph"]:
        year_graph.append([row["year"], row["citations"]])

    structure = {
        "number_of_articols": len(json_result["articles"]),
        "number_of_citations": json_result["cited_by"]["table"][0]["citations"]["all"],
        "h_index": json_result["cited_by"]["table"][1]["h_index"]["all"],
        "year_graph": year_graph,
    }

    print(structure)
