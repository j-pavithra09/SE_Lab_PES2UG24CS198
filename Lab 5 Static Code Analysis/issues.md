# Issues Identified in Static Code Analysis

| No. | Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|---|
| 1 | Use of eval() | Security - Medium | 12 | eval() evaluates a string as Python code and may execute unintended or malicious code. | Replace eval() with a safer formula evaluator that validates permitted operations. |
| 2 | Bare except | Error Handling - Low | 37-38 | The except block catches all exceptions and silently ignores them using pass. | Catch specific exceptions and handle errors explicitly. |
| 3 | Unused math import | Code Quality | 2 | The math module is imported but never used. | Remove the unused import. |
| 4 | Unused sys import | Code Quality | 3 | The sys module is imported but never used. | Remove the unused import. |
| 5 | Mutable default argument | Potential Bug | 14 | The logs=[] default creates a shared list across function calls. | Use logs=None and initialize a new list inside the function. |
| 6 | Boolean comparison | Code Style | 43 | Comparing a Boolean value with True is unnecessary. | Replace == True with a direct condition. |
| 7 | Missing input validation | Potential Bug / Security | 11-19, 31-33 | GPA, credits, income, and the custom merit formula are not adequately validated. | Validate input types and allowed ranges before calculating scores. |
| 8 | File handling without context manager | Code Quality / Reliability | 26-28, 36 | Files are opened without using a context manager. | Use with open() to ensure files are closed properly. |
| 9 | Incorrect blank-line spacing | Code Style | 11, 14, 24, 28, 33, 40, 46 | Functions do not follow the required blank-line spacing conventions. | Add the required blank lines between top-level functions. |
| 10 | Old-style string formatting | Code Style | 21 | The log message uses the older % formatting method. | Replace it with an f-string. |
| 11 | Non-standard function naming | Code Style | 40 | printShortlist() does not follow the snake_case naming convention. | Rename it to print_shortlist() and update its function call. |