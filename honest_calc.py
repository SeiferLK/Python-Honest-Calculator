def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()

def is_digit(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "-" or v3 == "+"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
    ]

opers = ["+", "-", "*", "/"]
flag = True
memory = 0
result = 0

while flag:
    print(msg_[0])
    x, oper, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if is_digit(y) and is_digit(x):
        x, y = float(x), float(y)
        if oper in opers:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            elif y == 0:
                print(msg_[3])
                continue
            print(result)
            while True:
                print(msg_[4])
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                    continue
                                else:
                                    memory = result
                                    break
                            elif answer == "n":
                                break
                            else:
                                continue
                    else:
                        memory = result
                elif answer != "n":
                    continue
                while True:
                    print(msg_[5])
                    answer = input()
                    if answer == "y":
                        break
                    elif answer == "n":
                        flag = False
                        break
                    else:
                        continue
                break
        else:
            print(msg_[2])
    else:
        print(msg_[1])
