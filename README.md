ResumeAnalyzer AI

ResumeAnalyzer AI is an intelligent agent built with Gemini ADK that evaluates, scores, and improves resumes. It provides section-wise feedback, rewrites weak bullet points, checks ATS compatibility, and gives actionable suggestions to help users create polished, competitive resumes.

Features

Resume Parsing: Automatically detects sections like Summary, Skills, Experience, Education, Projects, and Certifications.

Section Scoring: Scores each section based on clarity, conciseness, readability, and content impact.

Bullet Point Enhancement: Rewrites weak or generic bullet points using strong, measurable action verbs.

ATS Compatibility Check: Flags issues that may prevent your resume from being parsed correctly by automated systems.

Keyword Optimization: Suggests relevant keywords for your target job role.

Personalized Feedback: Provides guidance tailored to each section of your resume.

Project Structure
ResumeAnalyzerAI/
│
├── agent.yaml               # Gemini agent configuration
├── main.py                  # Entry point for the agent
├── utils/
│   ├── parser.py            # Resume parsing functions
│   ├── scorer.py            # Resume scoring logic
│   └── feedback.py          # AI feedback generation functions
├── prompts/
│   └── rewrite_prompt.txt   # Template for bullet rewriting & feedback
├── data/                    # Optional storage for resumes
├── requirements.txt         # Python dependencies
└── README.md

Installation

Clone the repository:

git clone https://github.com/your-username/ResumeAnalyzerAI.git
cd ResumeAnalyzerAI


Install dependencies:

pip install -r requirements.txt


Download spaCy English model:

python -m spacy download en_core_web_sm


Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

Usage

Start the Gemini ADK agent:

python main.py


Call the analyze_resume task with a resume text input:

from gemini import Client

client = Client()
resume_text = """
John Doe
Summary: Experienced software engineer...
Skills: Python, Flask, SQL...
Experience: Worked at ABC Corp...
Education: B.Tech in Computer Science...
"""
response = client.run_task("ResumeAnalyzerAI", "analyze_resume", {"resume_text": resume_text})
print(response)


The agent will return:

sections → Parsed resume sections

scores → Section-wise and total scores

feedback → Suggested improvements and rewritten bullet points

How It Works

Parse Resume: Extract structured sections from raw text.

Score Sections: Evaluate readability, conciseness, and content quality.

Generate Feedback: Use GPT to rewrite weak bullets and provide improvement suggestions.

Return Results: Section-wise rewritten content, scores, and actionable tips.
