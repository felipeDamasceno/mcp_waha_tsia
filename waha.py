from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("waha")

WAHA_URL = "http://localhost:3000/api/sendText"

@mcp.tool()
async def send_message(phone_number: str, message: str) -> str:
    """Send a WhatsApp message using WAHA.

    Args:
        phone_number: Phone number in international format (e.g. +5511999999999)
        message: The message to send
    """
    chat_id = phone_number.replace("+", "") + "@c.us"
    data = {
        "chatId": chat_id,
        "text": message,
        "session": "default"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(WAHA_URL, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return f"Message sent! Response: {response.json()}"
    except Exception as e:
        return f"Failed to send message: {e}"

if __name__ == "__main__":
    mcp.run(transport='stdio')