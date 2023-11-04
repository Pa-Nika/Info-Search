def pascal():
    tmp_row = [1]
    for _ in range(n):
        print(*tmp_row)
        new_row = [1]

        for j in range(1, len(tmp_row)):
            new_row.append(tmp_row[j - 1] + tmp_row[j])

        new_row.append(1)
        tmp_row = new_row


def bracket_sequence():
    stack = []

    for char in sequence:
        stack.append(char)
        if char == "(":
            pass
        elif char == ")" and len(stack) >= 2:
            if stack.pop() != ")" or stack.pop() != "(":
                print("Неправильная скобочная последовательность")
                return
        else:
            print("Неправильная скобочная последовательность")
            return

    if len(stack) != 0:
        print("Неправильная скобочная последовательность")
        return
    print("Правильная скобочная последовательность")
    return


def caesar_cipher(text, shift, language):
    result = ""
    alphabet = ""

    if language.lower() == "en":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif language.lower() == "ru":
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        print("Нет такого языка...")
        return

    for char in text:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            index = (alphabet.index(char.upper()) + shift) % len(alphabet)
            if is_upper:
                result += alphabet[index]
            else:
                result += alphabet[index].lower()
        else:
            result += char

    return result


def write_file():
    try:
        input_file_path = input("Введите путь до файла: ")
        shift = int(input("Введите сдвиг: "))
        language = input("Введите язык (en/ru): ")

        with open(input_file_path, "r", encoding="utf-8") as file:
            text = file.read()

        encrypted_text = caesar_cipher(text, shift, language)

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_text)

    except Exception as e:
        print("УУПС, что-то пошло не так", e)


if __name__ == "__main__":
    n = 0
    while n <= 0:
        try:
            n = int(input("Введите число n для треугольника Паскаля: "))
            if n <= 0:
                raise ValueError("Число должно быть положительным.")
            break
        except ValueError:
            print("Введите целое положительное число.")
    pascal()

    print("Введите скобочную последовательность:")
    sequence = str(input())
    bracket_sequence()

    write_file()
