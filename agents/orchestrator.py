from langchain.agents import Tool, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os

from agents.scorer import scorer_agent
from agents.feedback import feedback_agent
from agents.validator import validator_agent

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

tools = [
    Tool(name="Scorer", func=scorer_agent, description="Scores a transcript"),
    Tool(
        name="Feedback",
        func=lambda transcript: feedback_agent(transcript, scorer_agent(transcript)["score"]),
        description="Generates feedback"
    ),
    Tool(
        name="Validator",
        func=lambda transcript: validator_agent(
            transcript,
            scorer_agent(transcript)["score"],
            feedback_agent(transcript, scorer_agent(transcript)["score"])
        ),
        description="Validates score and feedback"
    )
]

agent = initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def orchestrate(transcript: str) -> dict:
    score_data = scorer_agent(transcript)
    score = score_data["score"]
    breakdown = score_data["breakdown"]

    feedback = feedback_agent(transcript, score)
    reasoning = validator_agent(transcript, score, feedback)

    return {
        "score": score,
        "feedback": feedback,
        "reasoning": reasoning,
        "breakdown": breakdown
    }