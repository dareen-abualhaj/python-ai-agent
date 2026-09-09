from functions.get_file_content import get_file_content

def main() -> None:
    # 1. اختبار ملف lorem.txt والتحقق من الاقتصاص
    result_lorem = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result_lorem)}")
    print(f"lorem.txt truncated: {'truncated' in result_lorem}")

    # 2. اختبار قراءة ملفات حقيقية داخل المشروع
    print("\n--- main.py content snippet ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- pkg/calculator.py content snippet ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # 3. اختبار الأخطاء (خارج المجلد أو ملف غير موجود)
    print("\n--- Error test: /bin/cat ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Error test: pkg/does_not_exist.py ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
