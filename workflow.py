from config import COURSE_FEES, QUESTIONS, banner


def workflow(question):

    question_lower = question.lower()

    # Rule 1: Single course fee
    if "fee" in question_lower and "ai202" in question_lower:

        return f"The fee for AI202 is Rs. {COURSE_FEES['AI202']}."

    # Rule 2: Total fee with scholarship
    if (
        "total" in question_lower
        and "cs101" in question_lower
        and "ai202" in question_lower
        and "10%" in question_lower
    ):

        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        final_amount = total * 0.90

        return (
            f"Total fee = Rs. {total}\n"
            f"After 10% scholarship = Rs. {final_amount:.0f}"
        )

    # Rule 3: Compare DS303 and CS101
    if (
        "ds303" in question_lower
        and "cs101" in question_lower
        and "expensive" in question_lower
    ):

        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]

        return (
            f"DS303 is more expensive than CS101 "
            f"by Rs. {difference}."
        )

    # Rule 4: Welcome message
    if "welcome" in question_lower:

        return (
            "Welcome to the College Course Assistant!\n"
            "We are happy to help you with course information."
        )

    return "Sorry, I can only answer predefined course-fee questions."


if __name__ == "__main__":

    banner("SYSTEM 2: RULE-BASED WORKFLOW")

    for question in QUESTIONS:

        print("\nQ:", question)

        answer = workflow(question)

        print("A:", answer)

        print("-" * 70)