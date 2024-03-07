def check_brackets(string):
    stack = []
    result = [' '] * len(string)
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack and string[stack[-1]] == '(':
                stack.pop()
            else:
                result[i] = '?'
    for i in stack:
        result[i] = 'x'
    return ''.join(result)

if __name__ == "__main__":
    while True:
        string = input("请输入一个字符串（输入'q'退出）：")
        if string.lower() == 'q':
            break
        print(string)
        print(check_brackets(string))
