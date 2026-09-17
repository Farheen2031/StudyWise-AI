"""
quiz_engine.py
Handles quiz scoring and answer review.
"""


def calculate_score(mcqs, user_answers):
    """
    Calculate the quiz score.

    Parameters:
        mcqs: List of generated MCQ dictionaries.
        user_answers: List of answers selected by the user.

    Returns:
        Dictionary containing score, total, percentage, and review.
    """

    if not isinstance(mcqs, (list, tuple)):
        mcqs = []

    if not isinstance(user_answers, (list, tuple)):
        user_answers = []

    total = len(mcqs)
    correct_count = 0
    review = []

    for i, mcq in enumerate(mcqs):

        if not isinstance(mcq, dict):
            question = "Invalid question"
            correct_answer = None
        else:
            question = mcq.get("question", "")
            correct_answer = mcq.get("correct_answer")

        if i < len(user_answers):
            user_answer = user_answers[i]
        else:
            user_answer = None

        is_correct = (
            correct_answer is not None
            and user_answer == correct_answer
        )

        if is_correct:
            correct_count += 1

        review.append({
            "question": question,
            "your_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })

    if total > 0:
        percentage = round((correct_count / total) * 100, 1)
    else:
        percentage = 0.0

    return {
        "score": correct_count,
        "total": total,
        "percentage": percentage,
        "review": review
    }