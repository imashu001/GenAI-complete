from google import genai
from google.genai import types

client = genai.Client()

def run_multi_agent_pipeline(user_query: str):
    # Step 1: Research Agent gathers information
    research_prompt = f"Gather comprehensive facts, data, and context on the following topic: {user_query}"
    research_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=research_prompt,
    )
    research_findings = research_response.text

    # Step 2: Content Builder Agent turns research into a structured report
    builder_prompt = f"""
    You are an expert technical writer. Take the following research findings 
    and transform them into a well-structured, engaging markdown report.

    Research Findings:
    {research_findings}
    """
    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=builder_prompt,
    )
    
    return final_response.text

# Run the pipeline
# result = run_multi_agent_pipeline("Latest advancements in Multi-Agent Systems")
# print(result)