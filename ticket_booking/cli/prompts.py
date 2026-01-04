def prompt_choice(title: str, options: list[str]) -> int:
    print("\n" + title)
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    while True:
        raw = input("Select an option: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw)
        print("Invalid choice. Try again.")

def prompt_text(label: str) -> str:
    return input(f"{label}: ").strip()
