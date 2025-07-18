# agent_scraper.py

import os
from typing import List, Optional
from pydantic import BaseModel, Field
from llama_index.llms.openai import OpenAI
from llama_index.program.openai import OpenAIPydanticProgram
from web_crawler_module import WebCrawler


# ----------- Pydantic Schema -----------

class OpenAIModelFee(BaseModel):
    product_list: List[str] = Field(..., description="List of products in the store")
    hero_products: List[str] = Field(..., description="List of hero products in the store")
    privacy_policy: Optional[str] = Field(None, description="Privacy policy of the store")
    return_policy: Optional[str] = Field(None, description="Return policy of the store")
    faqs: List[str] = Field(..., description="List of FAQs")
    social_handles: List[str] = Field(..., description="List of social media handles of the store")
    contact_emails: List[str] = Field(..., description="List of contact emails of the store")
    contact_numbers: List[str] = Field(..., description="List of contact numbers of the store")
    Brand_details_text: Optional[str] = Field(None, description="About text of the store")
    important_links: List[str] = Field(..., description="List of the important links of the store")


# ----------- Scraper Function -----------

def scrape_data(url: str) -> Optional[OpenAIModelFee]:
    """Scrape brand content from a given Shopify brand URL."""
    
    crawler = WebCrawler()
    crawler.warmup()

    try:
        result = crawler.run(url=url, word_count_threshodl=1, bypass_cache=True)
        full_context = result["text"] if isinstance(result, dict) else result

        llm = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

        program = OpenAIPydanticProgram.from_defaults(
            output_cls=OpenAIModelFee,
            llm=llm,
            prompt_template_str=f"""You are a data extraction expert. Extract the following information from the provided website content and return it as a valid JSON object.
            Required JSON Schema:
            {{
                "product_list": ["List of products in the store"],
                "hero_products": ["List of hero/featured products in the store"],
                "privacy_policy": "Privacy policy text or null",
                "return_policy": "Return policy text or null",
                "faqs": ["List of frequently asked questions"],
                "social_handles": ["List of social media handles/URLs"],
                "contact_emails": ["List of contact email addresses"],
                "contact_numbers": ["List of contact phone numbers"],
                "Brand_details_text": "About us/brand story text or null",
                "important_links": ["List of important website links"]
            }}

            Instructions:
            - Extract **all products**, not just a few examples.
            - **Hero products** are usually featured/highlighted products on the homepage.
            - Look for **full policy texts**, not just mentions.
            - Extract all **FAQs with full text**.
            - Include **all social media links** and handles.
            - Find all **contact methods** (emails, phones).
            - Extract the **complete brand story/about text**.
            - Include all **important navigation and policy links**.

            Website Content:
            \"\"\"
            {{context}}
            \"\"\"

            Return only a valid JSON matching the above structure.
             """
        )
        output = program(context=full_context)
        return output

    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")
        return None


