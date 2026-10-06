import random

CHOICES = ("سنگ", "کاغذ", "قیچی")
WINNING_RULES = {
    "سنگ": "قیچی",
    "کاغذ": "سنگ",
    "قیچی": "کاغذ",
}

def determine_winner(player: str, computer: str) -> str:
    if player == computer:
        return "مساوی"
    if WINNING_RULES[player] == computer:
        return "کاربر"
    return "کامپیوتر"


def main() -> None:
    print("گزینه‌ها:", "، ".join(CHOICES))
    player = input("انتخاب شما: ").strip()

    if player not in CHOICES:
        print("گزینه نامعتبر است.")
        return

    computer = random.choice(CHOICES)
    winner = determine_winner(player, computer)
    print("انتخاب کامپیوتر:", computer)
    print("نتیجه:", winner)


if __name__ == "__main__":
    main()