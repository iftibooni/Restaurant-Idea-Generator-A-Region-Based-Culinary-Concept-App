from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the loaded environment variables
api_key = os.getenv("OPENAI_API_KEY")

def resturant_Genearator(dish):
     
       # Initialize LLM
    llm = OpenAI(temperature=0.7)

    # 1. Chain to generate restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name"
    )

    # 2. Chain to generate menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 5 menu items for {restaurant_name}. Return as a comma-separated list."
    )
    food_items_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key="menu_items"
    )

    # 3. Combined chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        verbose=True  # Optional: shows execution steps
    )

    # 4. Execute the chain
    result = chain({'cuisine':dish})
        
    return result

