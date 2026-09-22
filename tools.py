from config import COURSE_FEES


def get_course_fee(course_code):

    course_code = course_code.upper()

    if course_code not in COURSE_FEES:
        return f"Unknown course code: {course_code}"

    return str(COURSE_FEES[course_code])


def calculator(expression):

    allowed = set(
        "0123456789+-*/(). "
    )

    if not all(char in allowed for char in expression):
        return "Invalid expression."

    try:

        result = eval(expression, {"__builtins__": {}}, {})

        return str(result)

    except Exception as error:

        return f"Calculation error: {error}"


TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee,
    "calculator": calculator
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course from the private college database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303."
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]