# Expression Evaluator Assignment

## Overview
This Python program reads mathematical expressions from `input.txt`, evaluates them using a stack-based approach (Shunting-Yard algorithm for infix to postfix conversion, followed by postfix evaluation), and writes the results to `output.txt`.

## How to Run
1. Place the `input.txt` file in the same directory as the script.
2. Ensure Python 3 is installed.
3. Run the program using: `python expression_evaluator.py`
4. The program will generate `output.txt` in the same directory.

## Structure of Input and Output Files
- **Input.txt**: Contains infix mathematical expressions, each on a separate line, separated by lines containing only `----`. Tokens (numbers, operators, parentheses) are separated by spaces. Example:
