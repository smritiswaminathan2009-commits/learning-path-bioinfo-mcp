RESOURCES = {
    "python": ["Python official tutorial", "CS50P (Harvard)", "Automate the Boring Stuff"],
    "machine learning": ["Andrew Ng ML Specialization", "fast.ai", "Kaggle Learn"],
    "bioinformatics": ["Rosalind problems", "Biopython tutorial", "Coursera Bioinformatics"],
}
LEVELS = {"beginner": "Fundamentals", "intermediate": "Projects", "advanced": "Depth"}

def generate_path(topic: str, level: str = "beginner", weeks: int = 4) -> dict:
    res = RESOURCES.get(topic.lower(), [f"Search: '{topic} for {level}s'", "YouTube crash course", "Official docs"])
    plan = []
    for w in range(1, weeks + 1):
        phase = "Foundations" if w <= weeks // 3 + 1 else "Practice" if w < weeks else "Capstone project"
        plan.append({"week": w, "focus": phase, "resource": res[(w - 1) % len(res)],
                     "goal": f"{LEVELS.get(level, 'Core')} of {topic}: {phase.lower()}"})
    return {"topic": topic, "level": level, "weeks": weeks, "plan": plan}
