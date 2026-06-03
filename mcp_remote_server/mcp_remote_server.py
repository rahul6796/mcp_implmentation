



from fastmcp import FastMCP
import random
import json


mcp = FastMCP(name = "Simple calculator server")

@mcp.tool
def add(a : int, b: int) -> int:
    """
    Add two numbers together 
    
    Agrs: 
        a : int (first no)
        b : int (second no)

    return:
        sum of this above two number.
    """

    return a + b


@mcp.tool
def randum_number(min_num: int, max_num: int) -> int:
    """
    Generate a randum number in this range.

    Args: 
        min_num: starting of the number.
        max_num: ending of the number.

    return:
        in between the min_num and max_mum
    """
    return random.randint(min_num, max_num)


@mcp.resource("info://server")
def server_info() -> str:

    """
    Get information about the server.
    """

    info = {

        "name": "Simple Calculator server",
        "version":" 1.0.0",
        "description":"A basic MCP server of math tools",
        "tools":["add", "randum_number"],
        "author": "Rahul Prajapati"
    }

    return json.dumps(info, indent=2)



# command for run. the remote server.

if __name__ == "__main__":
    mcp.run(
        transport = "http",
        host = "0.0.0.0",
        port = 5000
    )
    


    

