

import random
from fastmcp import FastMCP


mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dict: int = 1) -> list[int]:
    """ 
    Roll n_dice 6 sided dice and return the results.
    """

    return [random.randint(1, 6) for _ in range(n_dict)]

@mcp.tool
def add_numbers(a: float, b: float) -> int:

    """
    Adding two number together.
    """
    return a + b


if __name__ == "__main__":
    mcp.run()