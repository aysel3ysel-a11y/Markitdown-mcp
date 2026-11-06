from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown

mcp = FastMCP("MarkItDown Service")
md = MarkItDown()

@mcp.tool()
def convert_file_to_markdown(file_url: str) -> str:
    """تحويل أي ملف إلى نص Markdown باستخدام أداة MarkItDown"""
    result = md.convert(file_url)
    return result.text_content

if __name__ == "__main__":
    mcp.run(transport='sse')
