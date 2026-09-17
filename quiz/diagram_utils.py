"""
diagram_utils.py
Creates simple charts and concept diagrams for StudyWise AI.
"""

import math
import matplotlib.pyplot as plt


def create_score_pie_chart(correct, incorrect):
    """
    Create a pie chart showing correct and incorrect answers.
    """

    correct = max(0, int(correct))
    incorrect = max(0, int(incorrect))

    fig, ax = plt.subplots(figsize=(4, 4))

    total = correct + incorrect

    if total == 0:
        ax.text(
            0.5,
            0.5,
            "No quiz data",
            ha="center",
            va="center",
            fontsize=12
        )
        ax.axis("off")
        return fig

    labels = ["Correct", "Incorrect"]
    values = [correct, incorrect]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.0f%%",
        startangle=90
    )

    ax.axis("equal")

    return fig


def create_concept_diagram(topic, keywords):
    """
    Create a simple concept diagram.

    The topic is placed in the center and
    important keywords are placed around it.
    """

    topic = str(topic or "Study Material").strip()

    if not topic:
        topic = "Study Material"

    if isinstance(keywords, str):
        keywords = [keywords]

    unique_keywords = []

    for keyword in keywords or []:
        keyword = str(keyword).strip()

        if keyword and keyword.lower() not in [
            item.lower() for item in unique_keywords
        ]:
            unique_keywords.append(keyword)

    # Keep the diagram simple and readable.
    unique_keywords = unique_keywords[:8]

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis("off")

    # Central topic
    ax.scatter([0], [0], s=3000)

    ax.text(
        0,
        0,
        topic,
        ha="center",
        va="center",
        fontsize=10,
        weight="bold"
    )

    number_of_keywords = len(unique_keywords)

    if number_of_keywords == 0:
        return fig

    for i, keyword in enumerate(unique_keywords):

        angle = 2 * math.pi * i / number_of_keywords

        x = math.cos(angle)
        y = math.sin(angle)

        # Connection line
        ax.plot(
            [0, x],
            [0, y],
            linewidth=1
        )

        # Keyword node
        ax.scatter(
            [x],
            [y],
            s=1800
        )

        ax.text(
            x,
            y,
            keyword,
            ha="center",
            va="center",
            fontsize=8
        )

    return fig