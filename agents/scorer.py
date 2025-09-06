def scorer_agent(transcript: str) -> dict:
    clarity = 8.0 if len(transcript.split()) > 10 else 5.0
    relevance = 7.5 if "AI" in transcript.lower() else 6.0
    depth = 7.0 if any(word in transcript.lower() for word in ["reason", "impact", "future"]) else 5.5

    score = round((clarity * 0.4 + relevance * 0.3 + depth * 0.3), 2)

    return {
        "score": score,
        "breakdown": {
            "clarity": clarity,
            "relevance": relevance,
            "depth": depth
        }
    }