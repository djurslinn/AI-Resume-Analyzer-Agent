from gemini import Agent
from utils.parser import parse_resume
from utils.scorer import score_resume
from utils.feedback import generate_feedback

agent = Agent()

@agent.task("analyze_resume")
def analyze_resume(resume_text: str):
    sections = parse_resume(resume_text)
    scores = score_resume(sections)
    feedback = generate_feedback(sections)
    return {
        "sections": sections,
        "scores": scores,
        "feedback": feedback
    }

if __name__ == "__main__":
    agent.run()
