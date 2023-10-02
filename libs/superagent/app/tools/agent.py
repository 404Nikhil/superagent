from typing import Any

import aiohttp
import requests
from langchain.tools import BaseTool


class Agent(BaseTool):
    name = "Agent as a Tool"
    description = "useful for answering questions."

    def _run(self, input: Any) -> str:
        agent_id = self.metadata["agentId"]
        api_key = self.metadata["apiKey"]
        url = f"https://api.beta.superagent.sh/api/v1/agents/{agent_id}/invoke"
        headers = {
            "content-type": "application/json",
            "authorization": f"Bearer {api_key}",
        }
        data = {"enableStreaming": False, "input": str(input)}
        response = requests.post(url=url, headers=headers, json=data)
        output = response.json()
        return output.get("data")

    async def _arun(self, input: Any) -> str:
        agent_id = self.metadata["agentId"]
        api_key = self.metadata["apiKey"]
        url = f"https://api.beta.superagent.sh/api/v1/agents/{agent_id}/invoke"
        headers = {
            "content-type": "application/json",
            "authorization": f"Bearer {api_key}",
        }
        data = {"enableStreaming": False, "input": str(input)}
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, json=data) as response:
                output = await response.json()
        return output
