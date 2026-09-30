# Password Strength Checker

A simple Python cybersecurity project that evaluates password strength using common password-security rules.

## Features

- Checks minimum password length
- Checks uppercase letters
- Checks lowercase letters
- Checks numbers
- Checks special characters
- Calculates a score out of 5
- Classifies the password as Weak, Medium, or Strong
- Provides suggestions for improvement

## Technologies

- Python 3
- Regular Expressions (`re`)
- Functions
- Conditional Statements
- String Handling

## How to Run

Open Terminal in this project folder and run:

```bash
python password_checker.py
```

Then enter a password when prompted.

## Example

```text
Enter your password: Hello123

Password Analysis
-----------------
Strength: Medium
Score: 4/5

Suggestions:
- Add a special character.
```

## How It Works

```text
Enter Password
      |
      v
Check Length
      |
      v
Check Uppercase
      |
      v
Check Lowercase
      |
      v
Check Number
      |
      v
Check Special Character
      |
      v
Calculate Score
      |
      v
Weak / Medium / Strong
```

## Resume Description

**Password Strength Checker | Python**

Developed a Python-based password strength checker that evaluates passwords based on length, uppercase and lowercase characters, numbers, and special characters. Implemented regular expressions and conditional logic to calculate a strength score and provide basic password-security feedback.

## Interview Explanation

"I developed a Password Strength Checker using Python. The program takes a password as input and checks five conditions: minimum length, uppercase letters, lowercase letters, numbers, and special characters. Each satisfied condition increases the score. Based on the final score, the program classifies the password as weak, medium, or strong and gives suggestions for improvement."

## Note

This is an educational password-strength project. It does not store or transmit passwords and should not be treated as a complete enterprise password-security system.
