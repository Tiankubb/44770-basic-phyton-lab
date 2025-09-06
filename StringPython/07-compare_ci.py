text = input().strip()
second_char = text[-1].lower()
first_char = text[0].lower()
if first_char < second_char:
    print('A come before B')
elif first_char > second_char:
    print('A come after B')
else:
    print('A equals B')