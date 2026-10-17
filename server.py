from fastmcp import FastMCP
import json 

mcp = FastMCP("simple calculator")

@mcp.tool
def add (a:int , b:int)-> int:
    "add two number"
    return a+b

if __name__ == "__main__":
    mcp.run(transport='http',host = '0.0.0.0',port = 8000)