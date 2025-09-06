def explain_score(score: float, rubric: dict) -> str:
    if score >= 8:
        return "Score reflects high clarity, depth, and relevance per rubric."
    elif score >= 5:
        return "Score indicates moderate clarity and relevance, but limited depth."
    else:
        return "Score suggests the response lacks clarity and depth based on rubric."