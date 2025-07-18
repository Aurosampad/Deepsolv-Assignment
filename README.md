
# **DEEPSOLV ASSIGNMENT – Shopify Brand Intelligence and Competitor Insights Engine**

**Author**: Aurosampad Mohanty  
**Role**: Machine Learning Engineer  
**Project Type**: GenAI Developer Intern Assignment  
**Organization**: Deepsolv.ai

---

**📘 PROJECT SUMMARY**

This project is built as part of a GenAI Developer Internship assignment at Deepsolv.ai. It delivers a complete, modular Python-based solution for **extracting structured brand intelligence from Shopify-based e-commerce stores** and **analyzing their competitors** using a combination of web scraping, metadata parsing, and vector database embedding via **FAISS**.

The system uses API endpoints to deliver actionable data insights about a Shopify brand and stores competitor intelligence in a vector space, enabling semantic search and downstream LLM applications such as RAG (Retrieval-Augmented Generation).

---

**🚀 OBJECTIVES**

- Automate brand information extraction from Shopify websites using robust scraping techniques.
- Build RESTful APIs using Flask for interaction and integration.
- Use search heuristics and web crawling to discover real competitors.
- Store competitor brand data and vector embeddings using FAISS.
- Design an architecture that is clean, testable, extensible, and ready for production.

---

**🧠 CORE FEATURES**

**1. Shopify Brand Metadata Scraper**
- Scrapes key brand-related metadata from Shopify stores.
- Extracts:
  - Brand/store name
  - Product categories and types
  - Approximate product count
  - SEO metadata (title, meta-description)
  - Brand bio / about section
- Handles common exceptions, broken URLs, and malformed HTML pages.

**2. Competitor Analysis & Embedding**
- Dynamically queries search engines or relevant sources to find close competitors.
- Scrapes and validates competitor domains and basic metadata.
- **Stores competitors as vector embeddings using FAISS** for similarity search and ranking.
- Supports future use in LLM-based tools like RAG pipelines.

**3. FAISS Vector Database Integration**
- Embeds competitor brand metadata into a FAISS vector store using OpenAI or sentence transformers.
- Enables fast similarity search and semantic querying over known competitor brands.
- Prepares the system for downstream GenAI workflows.

**4. API Layer via Flask**
- `GET /scrape-brand?url=https://example-store.myshopify.com`  
  → Returns structured brand metadata from the given Shopify URL.

- `GET /scrape-competitors?brand=BrandName`  
  → Extracts and stores vectorized data of similar competitors.

- Modular endpoints are future-proof and Docker-deployable.

---

**🗂️ FILE STRUCTURE**

```

DEEPSOLV ASSIGNMENT/
│
├── .env                            # API keys and environment configs
├── app.py                          # Main launcher script
├── flask\_app.py                    # Flask REST API server
├── agent\_scraper\_two.py            # Competitor scraper agent
├── web\_crawler\_module.py           # Core logic for crawling/scraping Shopify data
├── RAG\_Implementation.py           # FAISS vector database interaction & embedding logic
├── **pycache**/                    # Python bytecode cache

```

---

**⚙️ TECH STACK USED**

| Component         | Tech Used                                 |
|------------------|--------------------------------------------|
| Language          | Python 3.10+                              |
| API Framework     | Flask                                     |
| Web Scraping      | BeautifulSoup, Requests                   |
| Vector DB         | FAISS (Facebook AI Similarity Search)     |
| Embedding Model   | OpenAI Embeddings / Sentence Transformers |
| Data Format       | JSON, CSV                                 |
| Config Management | python-dotenv (`.env`)                    |

---

**💻 INSTALLATION & USAGE**

**Step 1: Clone the repository**
```

git clone [https://github.com/your-username/deepsolv-assignment.git](https://github.com/your-username/deepsolv-assignment.git)
cd deepsolv-assignment

```

**Step 2: Set up virtual environment (recommended)**
```

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

```

**Step 3: Install dependencies**
```

pip install -r requirements.txt

```

**Step 4: Create `.env` file**
```

OPENAI\_API\_KEY=your\_openai\_key\_here
SERPER\_API\_KEY=your\_serper\_api\_key\_here

```

**Step 5: Run the Flask app**
```

python flask\_app.py

````

**Step 6: Test the endpoints**
Ex- `http://localhost:5000/scrape-brand?url=https://example-store.myshopify.com`
Ex- `http://localhost:5000/scrape-competitors?brand=ExampleBrand`

---

**📊 SAMPLE OUTPUT**

```json
{
  "brand_name": "Modern Apparel Co.",
  "product_categories": ["T-Shirts", "Accessories", "Outerwear"],
  "description": "Sustainable streetwear for eco-conscious youth.",
  "competitors": [
    {
      "name": "Streetify",
      "url": "https://streetify.com",
      "similarity_score": 0.87
    },
    {
      "name": "EcoThreads",
      "url": "https://ecothreads.com",
      "similarity_score": 0.83
    }
  ]
}
````

Competitors are returned in descending order of similarity using cosine distance from the FAISS store.

---

**📈 REAL-WORLD USE CASES**

* Integrate with internal business dashboards for **brand intelligence**.
* Power **AI product recommenders** or **brand vs brand comparison tools**.
* Use as a back-end service for marketing tools, brand audit platforms, and GenAI copilots.

---

**📄 LICENSE**

This project is licensed under the **MIT License**.
You're free to use, modify, and distribute it with proper attribution.

---





