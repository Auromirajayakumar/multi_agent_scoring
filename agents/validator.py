from utils.explain import explain_score

def validator_agent(transcript: str, score: float, feedback: str) -> str:
    rubric = {
        "clarity": 0.3,
        "depth": 0.4,
        "relevance": 0.3
    }
    return explain_score(score, rubric)