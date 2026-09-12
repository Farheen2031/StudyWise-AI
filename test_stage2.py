from ai_features.summary_generator import generate_summary
from ai_features.question_recommender import generate_important_questions
from ai_features.qa_engine import answer_question

sample_text = """
Photosynthesis is the process by which green plants convert sunlight into chemical energy.
It occurs mainly in the leaves, inside structures called chloroplasts.
Chlorophyll, the green pigment, absorbs sunlight and uses it to convert carbon dioxide and water into glucose and oxygen.
This process is essential for life on Earth because it produces the oxygen we breathe.
Plants release oxygen as a byproduct of photosynthesis.
The glucose produced is used by the plant as energy and to build new plant tissue.
Photosynthesis mainly occurs during daylight hours when sunlight is available.
"""

print("SUMMARY:")
print(generate_summary(sample_text, num_sentences=3))

print("\nIMPORTANT QUESTIONS:")
for q in generate_important_questions(sample_text, num_questions=4):
    print("-", q)

print("\nQ&A TEST:")
print(answer_question(sample_text, "What produces oxygen?"))
