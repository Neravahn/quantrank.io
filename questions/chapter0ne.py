import random
import math

def ratio_1():
    a = random.randint(2, 100)
    b = random.randint(2, 100)
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
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    gcd = math.gcd(a, b)

    a_s, b_s = a//gcd, b//gcd

    question = f"The duplicate ratio orf {a_s} : {b_s} is ?"
    answer = f"{a_s ** 2} : {b_s **2}"
    return question, answer

q, a = ratio_2()
print(q, a)



def ratio_3():
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    a_s_squared, b_s_squared = a_s ** 2, b_s ** 2

    question = f"The sub-duplicate ratio of {a_s_squared} : {b_s_squared} is ?"
    answer = F"{a_s} : {b_s}"
    return question, answer

q, a = ratio_3()
print(q, a)



def ratio_4():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    gcd = math.gcd(a, b)
    a_s, b_s = a//gcd, b//gcd
    
    question = f"The triplicate ratio of {a_s} : {b_s} is ?"
    answer = f"{a_s ** 3} : {b_s ** 3}"
    return question, answer

q, a = ratio_4()
print(q, a)


def ratio_5():
    a= random.randint(1, 10)
    b = random.randint(1, 10)
    gcd = math.gcd(a, b)

    a_s, b_s = a // gcd, b //gcd

    question = f"The sub-triplicate ratio of {a_s ** 3} : {b_s ** 3} is ?"
    answer = f"{a_s} : {b_s}"
    return question, answer

q, a = ratio_5()
print(q, a)


def ratio_6():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    gcd = math.gcd(a, b)
    a_s = a // gcd
    b_s = b//gcd

    c = random.randint(1, 10)
    d = random.randint(1, 10)
    gcd = math.gcd(c, d)
    c_s = c//gcd
    d_s = d//gcd

    question = f"The ratio compounded of {a_s} : {b_s} and the duplicate ratio of {c_s} : {d_s} is"

    f_a = (a_s) * (c_s ** 2)
    f_b = (b_s) * (d_s ** 2)
    f_g = math.gcd(f_a, f_b)
    answer = f"{f_a // f_g} : {f_b // f_g}"

    return question, answer

q, a = ratio_6()
print(q, a)


def ratio_7():

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    gcd= math.gcd(a, b)
    a_s = a // gcd
    b_s = b// gcd


    c = random.randint(1, 10)
    d = random.randint(1, 10)
    gcd = math.gcd(c, d)
    c_s = c// gcd
    d_s = d//gcd


    e = random.randint(1, 10)
    f = random.randint(1, 10)
    gcd = math.gcd(e, f)
    e_s = e // gcd
    f_s = f // gcd


    g = random.randint(1, 10)
    h = random.randint(1, 10)
    gcd = math.gcd(g, h)
    g_s = g//gcd
    h_s = h// gcd

    question = f"The ratio compunded of {a_s} : {b_s}, the duplicate ratio of{c_s} : {d_s} the triplicate ratio of{e_s} : {f_s} and {g_s} : {h_s}"
    f_a = (a_s) * (c_s ** 2) * (e_s ** 3) * (g_s)
    f_b = (b_s) * (d_s ** 2) * (f_s ** 3) * (h_s)
    gcd = math.gcd(f_a, f_b)
    answer = f"{f_a // gcd} : {f_b // gcd}"
    return question, answer

q, a = ratio_7()
print(q, a)