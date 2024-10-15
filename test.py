
import re

text = "Ни234!@#$%^&*()_+=жн+ий    ---- 3Нов![]~`№%:,.;()_+город--888==="
# text="Нижний Новгород"


start = r'[\w\D]'

pattern = r'^[a-zA-Zа-яА-ЯёЁ\s?|\-?a-zA-Zа-яА-ЯёЁ]+[\s|-]?+[0-9]*$'


# result = re.findall(r'[a-zA-Zа-яА-ЯёЁ\s?|\-?]', text)
# result = re.findall(r'[a-zA-Zа-яА-ЯёЁ\s\-]+[a-zA-Zа-яА-ЯёЁ]?+[\s]?|[-]?+(?:[0-9]$)', text)
result = re.findall(r'[a-zA-Zа-яА-ЯёЁ\s\-]', text)
print(result)
print(''.join(result))

# class StringUtils:

#     name_city_pattern = None


#     @staticmethod
#     def is_palindrome(string):
#         return string == string[::-1]
