from quiz.mcq_generator import generate_mcqs
from quiz.quiz_engine import calculate_score
from quiz.diagram_utils import (
    create_score_pie_chart,
    create_concept_diagram
)

import matplotlib.pyplot as plt


sample_text = """
Photosynthesis is the process by which green plants convert sunlight
into chemical energy. Chlorophyll is the green pigment that absorbs
sunlight and helps plants convert carbon dioxide and water into glucose
and oxygen. This process is essential for life on Earth because it
produces the oxygen we breathe. Plants release oxygen as a byproduct
of photosynthesis.
"""


# --------------------------------------------------
# Test 1: MCQ generation
# --------------------------------------------------

mcqs = generate_mcqs(sample_text, num_questions=3)

assert len(mcqs) > 0, "MCQ generation failed."
assert len(mcqs) <= 3, "Generated more questions than requested."

for mcq in mcqs:
    assert "question" in mcq
    assert "options" in mcq
    assert "correct_answer" in mcq

    assert mcq["correct_answer"] in mcq["options"]
    assert len(mcq["options"]) == len(set(mcq["options"]))


print("MCQ generation test: PASSED")


# --------------------------------------------------
# Test 2: Perfect score
# --------------------------------------------------

correct_answers = [
    mcq["correct_answer"]
    for mcq in mcqs
]

perfect_result = calculate_score(
    mcqs,
    correct_answers
)

assert perfect_result["score"] == perfect_result["total"]
assert perfect_result["percentage"] == 100.0

print("Perfect score test: PASSED")


# --------------------------------------------------
# Test 3: Zero score
# --------------------------------------------------

wrong_answers = [
    None
    for _ in mcqs
]

zero_result = calculate_score(
    mcqs,
    wrong_answers
)

assert zero_result["score"] == 0
assert zero_result["percentage"] == 0.0

print("Zero score test: PASSED")


# --------------------------------------------------
# Test 4: Empty input
# --------------------------------------------------

assert generate_mcqs("", 3) == []

print("Empty input test: PASSED")


# --------------------------------------------------
# Test 5: Empty quiz scoring
# --------------------------------------------------

empty_result = calculate_score([], [])

assert empty_result["score"] == 0
assert empty_result["total"] == 0
assert empty_result["percentage"] == 0.0

print("Empty quiz test: PASSED")


# --------------------------------------------------
# Test 6: Diagram functions
# --------------------------------------------------

score_chart = create_score_pie_chart(2, 1)

concept_chart = create_concept_diagram(
    "Photosynthesis",
    ["sunlight", "chlorophyll", "oxygen"]
)

assert score_chart is not None
assert concept_chart is not None

plt.close(score_chart)
plt.close(concept_chart)

print("Diagram functions test: PASSED")


# --------------------------------------------------
# Final result
# --------------------------------------------------

print()
print("====================================")
print("STAGE 3 CORE TESTS PASSED")
print("====================================")