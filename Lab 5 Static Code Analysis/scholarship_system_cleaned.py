
"""Screen scholarship applicants and calculate their merit scores safely."""

import ast
import json
import operator

# Application settings and results
SETTINGS = {"merit_formula": "gpa * 10 + credits * 2"}
results = {}
INCOME_LIMIT = 800000
CUTOFF = 85

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def calculate_merit_score(gpa, credit_points):
    """Calculate merit using a restricted arithmetic formula."""
    expression = ast.parse(SETTINGS["merit_formula"], mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Only numeric constants are allowed.")

        if isinstance(node, ast.Name):
            values = {"gpa": gpa, "credits": credit_points}
            if node.id in values:
                return values[node.id]
            raise ValueError(f"Unknown variable: {node.id}")

        if isinstance(node, ast.BinOp):
            operation = ALLOWED_OPERATORS.get(type(node.op))
            if operation is None:
                raise ValueError("Arithmetic operation not allowed.")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)):
                if right == 0:
                    raise ValueError("Division by zero is not allowed.")

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            operation = ALLOWED_OPERATORS.get(type(node.op))
            if operation is not None:
                return operation(evaluate(node.operand))

        raise ValueError("Unsupported expression in merit formula.")

    return evaluate(expression)


def evaluate_applicant(student_id, test_scores, logs=None):
    """Evaluate an applicant and record the result."""
    if logs is None:
        logs = []

    gpa = test_scores["gpa"]
    credit_points = test_scores.get("credits", 0)
    income = test_scores.get("income", 0)

    score = calculate_merit_score(gpa, credit_points)
    eligible = score >= CUTOFF and income < INCOME_LIMIT

    results[student_id] = {
        "score": score,
        "eligible": eligible,
    }

    logs.append(f"{student_id} scored {score}")
    return eligible


def change_formula(new_formula):
    """Validate and update the merit formula."""
    previous_formula = SETTINGS["merit_formula"]
    SETTINGS["merit_formula"] = new_formula

    try:
        calculate_merit_score(1, 1)
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError):
        SETTINGS["merit_formula"] = previous_formula
        raise ValueError("Invalid merit formula.") from None


def persist_results(file="scholarships.json"):
    """Save applicant results to a JSON file."""
    with open(file, "w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=4)


def load_results(file="scholarships.json"):
    """Load applicant results from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as input_file:
            loaded_results = json.load(input_file)
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        print("Warning: Results file contains invalid JSON.")
        return

    if isinstance(loaded_results, dict):
        results.clear()
        results.update(loaded_results)
    else:
        print("Warning: Results file must contain a JSON object.")


def print_shortlist():
    """Print shortlisted applicants."""
    print("Shortlisted applicants:")
    for student_id, applicant in results.items():
        if applicant["eligible"]:
            print(f"  {student_id} score = {applicant['score']}")


def main():
    """Run the scholarship screening program."""
    evaluate_applicant(
        "U001", {"gpa": 9.1, "credits": 4, "income": 450000}
    )
    evaluate_applicant(
        "U002", {"gpa": 7.2, "credits": 1, "income": 300000}
    )
    evaluate_applicant(
        "U003", {"gpa": 12.5, "credits": -3, "income": -1}
    )
    evaluate_applicant("U004", {"gpa": 6.5})

    formula = input("Merit formula (Enter to keep default): ")
    if formula:
        try:
            change_formula(formula)
        except ValueError as error:
            print(f"Invalid formula: {error}")
            return

    evaluate_applicant(
        "U005", {"gpa": 8.4, "credits": 3, "income": 600000}
    )

    persist_results()
    load_results()
    print_shortlist()


if __name__ == "__main__":
    main()
