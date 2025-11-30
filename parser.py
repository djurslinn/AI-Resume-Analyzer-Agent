import re

def parse_resume(text):
    sections = {}
    headers = ["summary", "objective", "skills", "experience", "education", "projects", "certifications"]
    for header in headers:
        pattern = re.compile(f"{header}[:\\n]", re.IGNORECASE)
        match = pattern.search(text)
        if match:
            start = match.end()
            end = len(text)
            for nh in headers:
                if nh == header:
                    continue
                nh_match = re.search(f"{nh}[:\\n]", text[start:], re.IGNORECASE)
                if nh_match:
                    end = start + nh_match.start()
                    break
            sections[header.capitalize()] = text[start:end].strip()
        else:
            sections[header.capitalize()] = ""
    return sections
