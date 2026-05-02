import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

def create_research_agent():
    """
    Initializes and returns a LangChain AgentExecutor using Groq and Tavily.
    """
    # 1. Initialize the LLM (llama-3.1-8b-instant via Groq)
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # 2. Initialize the search tool
    search_tool = TavilySearchResults(max_results=3)
    tools = [search_tool]
    
    # 3. Create the prompt for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful and detailed research assistant. Use the search tool to find accurate and up-to-date information."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    # 4. Construct the tool calling agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # 5. Create an agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    return agent_executor

def run_research(query: str) -> str:
    """
    Runs the agent with the given query and returns the output.
    """
    agent_executor = create_research_agent()
    response = agent_executor.invoke({"input": query})
    return response.get("output", "No response generated.")

if __name__ == "__main__":
    # Test the agent locally
    query = "What is the capital of France?"
    print(f"Query: {query}")
    print("Response:", run_research(query))
