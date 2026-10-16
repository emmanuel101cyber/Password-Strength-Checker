Overview

A Python-based password strength analyzer developed as a cybersecurity learning project. It evaluates password characteristics and provides recommendations to help users create stronger passwords.

Features
Password length analysis
Character composition analysis
Detection of selected common passwords
Detection of predictable sequences
Detection of repeated characters
Password strength rating and recommendations
Local analysis without saving the entered password
Technologies
Python 3
Kali Linux
Git and GitHub
Installation

Clone this repository:

git clone https://github.com/emmanuel101cyber/Password-Strength-Checker.git
cd Password-Strength-Checker
Usage

Run the program:

python3 password_checker.py

Enter a made-up test password when prompted. The input is hidden while typing.

Testing

Test with different examples, including:

Common passwords
Short passwords
Passwords with predictable sequences
Longer passwords with varied characters

Never use a real password for testing.

Limitations

This tool uses heuristic scoring and a small built-in list of common passwords. Its ratings are estimates, not guarantees of password security. Character-distribution entropy is not the same as the total entropy of a password or its actual resistance to cracking.

Learning Objectives
Practice Python programming
Understand basic password security principles
Identify common password weaknesses
Document a cybersecurity project using GitHub
Disclaimer

This project is for educational and defensive security purposes. It is not a substitute for a professional password-strength estimation tool.# Password-Strength-Checker
A Python-based password strength analyzer developed for cybersecurity learning.
