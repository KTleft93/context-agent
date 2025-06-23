from langchain.tools import Tool
from langchain_community.utilities import SerpAPIWrapper
import os

def get_search_tool():
    os.environ["SERPAPI_API_KEY"] = "f92335fcddd969d1f2918310ca021442e5060b56001a922a130a95da287fd97d"
    search = SerpAPIWrapper()
    return Tool(
        name="google_search",
        func=search.run,
        description="Useful for retrieving external knowledge via Google search."
    )
