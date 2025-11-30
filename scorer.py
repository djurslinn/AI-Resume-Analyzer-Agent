import textstat

def score_resume(sections):
    scores = {}
    for sec, text in sections.items():
        if not text:
            scores[sec] = 0
        else:
            readability = textstat.flesch_reading_ease(text)
            length_score = min(len(text.split()) / 100, 1) * 100
            scores[sec] = round((readability + length_score) / 2, 2)
    scores["Total"] = round(sum(scores.values()) / len(sections), 2)
    return scores
