from analyzer import TextAnalyzer

def main():
    print("=== ANALISIS TEKS OTOMATIS ===")
    print("Masukkan teks (akhiri dengan ENTER 2x):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    analyzer = TextAnalyzer(text)
    result = analyzer.analyze()

    print("\n=== HASIL ANALISIS ===")
    print(f"Jumlah baris: {result['lines']}")
    print(f"Jumlah kata: {result['words']}")

    print("\n5 Kata paling sering:")
    for word, count in result["top_words"]:
        print(f"- {word}: {count}")

    print(f"\nJumlah vokal: {result['vowels']}")
    print(f"Jumlah konsonan: {result['consonants']}")

if __name__ == "__main__":
    main()