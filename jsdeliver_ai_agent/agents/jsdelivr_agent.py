from pydantic_ai import Agent 
from tools.jsdelivr_tools import getAvailableTools 
from prompts.jsdelivr_prompt import SYSTEM_PROMPT 
from dotenv import load_dotenv 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = getAvailableTools(),
    system_prompt = SYSTEM_PROMPT
)

async def analyseJSDelivrRepos(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')