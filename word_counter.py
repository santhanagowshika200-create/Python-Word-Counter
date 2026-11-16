def read_file(filename):
    """Read and return the contents of a text file, or None if not found."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"\nError: The file '{filename}' was not found. Please check the name and try again.")
        return None
    except PermissionError:
        print(f"\nError: Permission denied when trying to read '{filename}'.")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None


def analyze_text(content):
    """Count lines, words, and characters in the given text."""
    # Count lines (splitlines handles \n and \r\n cleanly)
    lines = content.splitlines()
    total_lines = len(lines)

    # Count words (split() splits by any whitespace and ignores extra spaces)
    words = content.split()
    total_words = len(words)

    # Count characters (including and excluding spaces)
    total_chars_with_spaces = len(content)
    total_chars_without_spaces = len(content.replace(" ", "").replace("\n", "").replace("\r", ""))

    return {
        "lines": total_lines,
        "words": total_words,
        "chars_with_spaces": total_chars_with_spaces,
        "chars_without_spaces": total_chars_without_spaces
    }


def display_results(filename, stats):
    """Print the word, character, and line counts in a clear format."""
    print("\n========================================")
    print(f"File Analysis: {filename}")
    print("========================================")
    print(f"Total Lines:                  {stats['lines']}")
    print(f"Total Words:                  {stats['words']}")
    print(f"Total Characters (with spaces): {stats['chars_with_spaces']}")
    print(f"Total Characters (no spaces):   {stats['chars_without_spaces']}")
    print("========================================")


def main():
    print("========================================")
    print("          PYTHON WORD COUNTER           ")
    print("========================================")

    while True:
        filename = input("\nEnter the text file name (or 'q' to quit): ").strip()

        if filename.lower() in ('q', 'quit', 'exit'):
            print("Exiting Word Counter. Goodbye!")
            break

        if not filename:
            print("File name cannot be empty. Please try again.")
            continue

        content = read_file(filename)

        if content is not None:
            stats = analyze_text(content)
            display_results(filename, stats)


if __name__ == "__main__":
    main()