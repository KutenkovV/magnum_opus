def analyze_text():
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read().lower()

    letters = [char for char in text if 'a' <= char <= 'z']

    total_letters = len(letters)

    if total_letters == 0:
        open("analysis.txt", "w").close()
        return

    from collections import Counter
    counts = Counter(letters)

    frequencies = []
    for letter, count in counts.items():
        share = count / total_letters
        frequencies.append((letter, share))

    frequencies.sort(key=lambda x: (-x[1], x[0]))

    with open("analysis.txt", "w", encoding="utf-8") as file:
        for letter, share in frequencies:
            file.write(f"{letter} {share:.3f}\n")


analyze_text()