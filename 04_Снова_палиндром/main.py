from collections import Counter

def can_form_palindrome(s):
    counts = Counter(s)
    
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    
    if odd_count <= 1:
        return "Можно сделать палиндром"
    else:
        return "Нельзя сделать палиндром"


text = input("Введите строку: ")
print(can_form_palindrome(text))