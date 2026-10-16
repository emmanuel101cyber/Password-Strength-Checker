import getpass
import math
import re
import string
from collections import Counter

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123",
    "changeme",
    "password1",
    "1234567890",
}

SEQUENCES = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
)


def shannon_entropy(password):
    if not password:
        return 0.0

    counts = Counter(password)
    length = len(password)

    return -sum(
        (count / length) * math.log2(count / length)
        for count in counts.values()
    )


def contains_sequence(password, minimum=4):
    value = password.lower()

    for sequence in SEQUENCES:
        for candidate in (sequence, sequence[::-1]):
            for start in range(len(candidate) - minimum + 1):
                fragment = candidate[start:start + minimum]

                if fragment in value:
                    return True

    return False


def repeated_character_run(password, minimum=4):
    pattern = r"(.)\1{" + str(minimum - 1) + r",}"
    return bool(re.search(pattern, password))


def analyze_password(password):
    feedback = []
    normalized = password.lower()
    length = len(password)

    if not password:
        return {
            "score": 0,
            "rating": "Very Weak",
            "feedback": ["Enter a password to analyze."],
            "length": 0,
            "character_entropy": 0.0,
        }

    score = 0

    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use a longer password, preferably 15+ characters.")

    categories = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
        any(c.isspace() for c in password),
    ]

    score += sum(categories)

    if sum(categories) < 3:
        feedback.append(
            "Consider using a longer, less predictable password or passphrase."
        )

    if normalized in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password. Choose a unique one.")

    if repeated_character_run(password):
        score -= 2
        feedback.append("Avoid long runs of repeated characters.")

    if contains_sequence(password):
        score -= 2
        feedback.append("Avoid predictable sequences such as abcd or 1234.")

    if len(set(password)) <= 2 and length >= 4:
        score -= 2
        feedback.append("Use a greater variety of characters.")

    score = max(0, min(score, 8))

    if normalized in COMMON_PASSWORDS or score <= 1 or length < 8:
        rating = "Very Weak"
    elif score <= 3:
        rating = "Weak"
    elif score <= 5:
        rating = "Moderate"
    elif score <= 6:
        rating = "Strong"
    else:
        rating = "Very Strong"

    if not feedback:
        feedback.append(
            "No obvious issues detected. Use a unique password "
            "and consider a password manager."
        )

    return {
        "score": score,
        "rating": rating,
        "feedback": feedback,
        "length": length,
        "character_entropy": round(shannon_entropy(password), 2),
    }


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)
    print("Analysis runs locally. Input is not saved.")
    print("Use a made-up test password, not a real one.\n")

    password = getpass.getpass("Enter a test password: ")
    result = analyze_password(password)

    print("\n--- Analysis Results ---")
    print(f"Strength: {result['rating']}")
    print(f"Length: {result['length']} characters")
    print(f"Score: {result['score']}/8")
    print(f"Character-distribution entropy: "
          f"{result['character_entropy']} bits")

    print("\nRecommendations:")
    for item in result["feedback"]:
        print(f"- {item}")

    print("\nNote: This is a heuristic assessment, not a guarantee "
          "of resistance to password cracking.")


if __name__ == "__main__":
    main()
