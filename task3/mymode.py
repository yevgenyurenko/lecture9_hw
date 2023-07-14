def count_lines(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        return len(lines)
def count_characters(input_file):
    with open(input_file, 'r') as file:
        characters = file.read()
        return len(characters)
def test(name):
    lines = count_lines(name)
    chars = count_characters(name)
    print("Line count:", lines)
    print("Character count:", chars)

