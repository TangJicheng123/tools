import re

def extract_numbers_from_string(input_string):
    # 使用正则表达式找到连续的数字部分
    numbers = re.findall(r'\d+', input_string)
    
    # 将提取的数字部分转换为整数
    numbers_as_integers = [int(num) for num in numbers]
    if len(numbers_as_integers) > 0:
        return numbers_as_integers[-1]
    return -1

input_string = "There are 123 apples and 456 oranges in the basket."
numbers = extract_numbers_from_string(input_string)
print(numbers)