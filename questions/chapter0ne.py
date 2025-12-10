import random
import math

def ratio_1():
    a = random.randint(3, 100)
    b = random.randint(3, 100)
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    x = random.randint(1, 100)
    c = a_s * x

    question = f"The ratio of two quantities is {a_s} : {b_s}. If the antecedent is {c}, the consequent is ?"
    answer = b_s * x
    return question, answer

q, a = ratio_1()
print(q, a)



def ratio_2():
    a = random.randint(3, 100)
    b = random.randint(3, 100)
    gcd = math.gcd(a, b)

    a_s, b_s = a//gcd, b//gcd

    question = f"The duplicate ratio orf {a_s} : {b_s} is ?"
    answer = f"{a_s ** 2} : {b_s **2}"
    return question, answer

q, a = ratio_2()
print(q, a)



def ratio_3():
    a = random.randint(3, 100)
    b = random.randint(3, 100)
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    a_s_squared, b_s_squared = a_s ** 2, b_s ** 2

    question = f"The sub-duplicate ratio of {a_s_squared} : {b_s_squared} is ?"
    answer = F"{a_s} : {b_s}"
    return question, answer

q, a = ratio_3()
print(q, a)
