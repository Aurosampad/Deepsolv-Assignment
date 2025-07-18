from fastapi import FastAPI, HTTPException, Query
from agent_scraper_two import scrape_data
from RAG_Implementation import query_brand_index,store_in_vector_store

app = FastAPI()

@app.get("/scrape-brand")
def scrape_brand(url: str = Query(..., description="URL of the Shopify brand site")):
    try:
        data = scrape_data(url)
        if not data:
            raise HTTPException(status_code=401, detail="Website could not be scraped")
        store_in_vector_store(data)
        return {"status": "success", "message": "Data scraped and stored"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get-brand-context")
def get_context(prompt: str = Query(..., description="Your question or requirement from brand")):
    try:
        response = query_brand_index(prompt)
        return {"brand_context": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

