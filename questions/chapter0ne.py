import random

def ratio_1():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    x = random.randint(1, 9)
    c = a * x

    question = f"The ratio of two quatities is {a} : {b}. If the antecedent id {c}, the consequent is ?"
    answer = b * x
    return question, answer

q, a = ratio_1()
print(q, a)