import json
from pathlib import Path

DATA_FILE = Path("todo.json")


def load_tasks() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks: list[dict]) -> None:
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("The to-do list is empty.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "○"
        print(f"{index}. {status} {task['title']}")


def main() -> None:
    tasks = load_tasks()

    while True:
        print("\n 1.show  2. add  3. done  4. delete  5. exit")
        choice = input("Selection: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Job Title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
        elif choice in {"3", "4"}:
            show_tasks(tasks)
            try:
                index = int(input("Job Number: ")) - 1
                if not 0 <= index < len(tasks):
                    raise IndexError
                if choice == "3":
                    tasks[index]["done"] = True
                else:
                    tasks.pop(index)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("The number is invalid.")
        elif choice == "5":
            break
        else:
            print("The option is not valid.")


if __name__ == "__main__":
    main()