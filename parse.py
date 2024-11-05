import openai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/Users/sarka/AI_WEB_SCRAPPER/sample.env")
# Load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt template for extracting information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            # Format the prompt with the current DOM chunk and description
            prompt = template.format(dom_content=chunk, parse_description=parse_description)

            # Call the OpenAI API to get the response
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            # Extract the parsed content from the response
            parsed_content = response['choices'][0]['message']['content'].strip()
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(parsed_content)

        except Exception as e:
            # Catch any exception and log it
            print(f"An error occurred during parsing: {e}")
            break

    return "\n".join(parsed_results)
