#  Multi-Agent Transcript Scoring System

This project demonstrates how multiple AI agents can work together to evaluate the quality of a written transcript. It simulates how an intelligent tutor might assess a student's response by:

- Scoring it based on clarity, relevance, and depth
- Generating constructive feedback using an LLM
- Validating the reasoning behind the score and feedback

The system is modular, explainable, and built for demo-readiness using FastAPI, LangChain, and OpenAI.

---

##  Features

- **Rubric-Based Scoring**: Evaluates clarity, relevance, and depth using a custom scoring agent.
- **LLM Feedback Agent**: Generates constructive feedback based on the transcript and score.
- **Validator Agent**: Checks alignment between score, feedback, and transcript content.
- **Notebook Demo**: Interactive Jupyter notebook (`agent_comparison.ipynb`) for clean, step-by-step execution.

---

## 📁 Project Structure
multi_agent_scoring/ ├── agents/ │   ├── scorer.py │   ├── feedback.py │   └── validator.py ├── notebooks/ │   └── agent_comparison.ipynb ├── main.py ├── .env.example ├── requirements.txt

---

##  How to Run

## 1. Clone the repo:

   git clone https://github.com/Auromirajayakumar/multi_agent_scoring.git
   cd multi_agent_scoring
## 2.Create and activate a virtual environment:
python -m venv .venv
.\.venv\Scripts\activate


## 3.Install dependencies:
pip install -r requirements.txt
## 4. Add your OpenAI key to .env:
OPENAI_API_KEY=your-api-key-here


## 5. Launch the notebook:
jupyter notebook
## Sample Output
Rubric Score: 7.2
Breakdown: {'clarity': 8.0, 'relevance': 7.5, 'depth': 7.0}
LLM Feedback: "Clear and relevant, but could benefit from deeper analysis."
Validator Reasoning: "Score and feedback align with transcript intent."
## Tech Stack
- Python 3.13+
- FastAPI
- LangChain
- OpenAI API
- Jupyter Notebook
## Contact

- GitHub: [Auromirajayakumar](https://github.com/Auromirajayakumar)
- LinkedIn: [auromira-jayakumar](https://www.linkedin.com/in/auromira-jayakumar-1805aa2a9)






- 




