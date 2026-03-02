def count_unique_characters(message: str) -> int:
    message = message.lower()
    
    char_count = {}
    for char in message:
        char_count[char] = char_count.get(char, 0) + 1

    unique_count = 0
    for count in char_count.values():
        if count == 1:
            unique_count += 1

    return unique_count

print("Количество уникальных символов в строке:", count_unique_characters("аа"))        # 0
print("Количество уникальных символов в строке:", count_unique_characters("abc"))       # 3
print("Количество уникальных символов в строке:", count_unique_characters("aAbBc"))     # 1
print("Количество уникальных символов в строке:", count_unique_characters("Hello"))     # 3