from functions.run_python_file import run_python_file

def main() -> None:
    print("--- 1. main.py (no args) ---")
    print(run_python_file("calculator", "main.py"))

    print("\n--- 2. main.py with arg '3 + 5' ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\n--- 3. tests.py ---")
    print(run_python_file("calculator", "tests.py"))

    print("\n--- 4. Error: outside directory ../main.py ---")
    print(run_python_file("calculator", "../main.py"))

    print("\n--- 5. Error: nonexistent file ---")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\n--- 6. Error: not a python file (lorem.txt) ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main()
