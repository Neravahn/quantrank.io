import random
import math
from sub_supScript import sub_num, sub_text, sup_num, sup_text

def ratio_1():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    x = random.randint(1, 20)
    c = a_s * x

    question = f"The ratio of two quantities is {a_s} : {b_s}. If the antecedent is {c}, the consequent is ?"
    answer = b_s * x

    options = []
    while len(options) < 4:
        option = random.randint(2, 20)
        if option not in options and option != answer:
            options.append(option)
        else :
            continue

    random_pop = random.randint(0, 3)
    options.pop(random_pop)
    options.insert(random_pop, answer)
    
    return question, options, answer

q, o, a = ratio_1()
print(q, o, a)




def ratio_2():
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    gcd = math.gcd(a, b)

    a_s, b_s = a//gcd, b//gcd

    question = f"The duplicate ratio orf {a_s} : {b_s} is ?"
    answer = f"{a_s ** 2} : {b_s **2}"
    return question, answer



def ratio_3():
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    a_s_squared, b_s_squared = a_s ** 2, b_s ** 2

    question = f"The sub-duplicate ratio of {a_s_squared} : {b_s_squared} is ?"
    answer = F"{a_s} : {b_s}"
    return question, answer



def ratio_4():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    gcd = math.gcd(a, b)
    a_s, b_s = a//gcd, b//gcd
    
    question = f"The triplicate ratio of {a_s} : {b_s} is ?"
    answer = f"{a_s ** 3} : {b_s ** 3}"
    return question, answer



def ratio_5():
    a= random.randint(1, 10)
    b = random.randint(1, 10)
    gcd = math.gcd(a, b)

    a_s, b_s = a // gcd, b //gcd

    question = f"The sub-triplicate ratio of {a_s ** 3} : {b_s ** 3} is ?"
    answer = f"{a_s} : {b_s}"
    return question, answer



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



def ratio_8():
    a_s = random.randint(3, 10)
    b_s = random.randint(3, 10)
    gcd = math.gcd(a_s, b_s)
    a_s_gcd = a_s//gcd
    b_s_gcd = b_s//gcd


    k = random.randint(4, 8)
    a = a_s_gcd * k
    b = b_s_gcd * k

    x = random.randint(5, 10)
    c = a - x
    d = b - x
    gcd = math.gcd(c, d)
    c_s = c//gcd
    d_s = d//gcd


    question = f"Two numbers are in ratio {a_s_gcd} : {b_s_gcd}. If {x} be subtracted from each, they are in the ratio {c_s} : {d_s}. The numbers are ?"
    answer = f"({a}, {b})"

    return question, answer



def ratio_9():
    angle = 180
    x = 0
    while True:
        divisor = random.randint(5, 20)
        if angle % divisor == 0:
            x = divisor
            break
        else:
            continue

    div_angle = 180 // x
    while True:
        a = random.randint(2, 50)
        b = random.randint(2, 50)
        c = random.randint(2, 50)

        if a + b + c == div_angle:
            break
        else:
            continue

    question = f"The angles of a triangle are in ratio {a} : {b} : {c}. Find the angles"
    answer = f"({a * x}, {b * x}, {c * x})"
    return question, answer



def ratio_10():
    a = random.randint(2, 20)
    b = random.randint(2, 20)

    x = random.randint(20, 50)

    total_amt = (a * x) + (b * x)

    question = f"Division of {total_amt}$ between X and Y is in ratio {a} : {b}. X and Y would get ?"
    answer = f"({a * x}, {b * x})"

    return question, answer



def ratio_11():
    amt1 = random.randint(200, 500)
    hr1 = random.randint(5, 20)
    amt2 = random.randint(200, 500)
    hr2 = random.randint(5, 20)

    perhr_val1 = round(amt1 / hr1)
    perhr_val2 = round(amt2 / hr2)

    gcd = math.gcd(perhr_val1, perhr_val2)
    perhr_val1_gcd = perhr_val1 // gcd
    perhr_val2_gcd = perhr_val2 // gcd

    question = f"Anand earns {amt1} in {hr1} hrs and Promode {amt2} in {hr2}hrs. The ratio of their earnings is ( round off if necessary)"
    answer = f"{perhr_val1_gcd} : {perhr_val2_gcd}"
    return question, answer



def ratio_12():
    a = random.randint(3, 15)
    b = random.randint(3, 15)

    x = random.randint(20, 90)
    
    d = abs((a*x) - (b*x))

    question = f"The ratio of two numbers is {a} : {b}, their diffrence is {d}. Find the numbers"
    answer = f"{a*x}, {b*x}"
    return question, answer



def ratio_13():
    a = random.randint(3, 20)
    b = random.randint(3, 20)
    c = random.randint(3, 20)
    d = random.randint(3, 20)


    question = f"P, Q and R are three cities. The ratio of average temprature between P and Q is {a} : {b} and that between P and R is {c} : {d}. The ratio between temprature of Q and R is ?"
    gcd = math.gcd((a *d), (b * c))
    z = (a * d) // gcd
    y = (b * c) // gcd

    answer = f"{y} : {z}"
    return question , answer




def ratio_14():
    x = random.randint(2, 20)
    y = random.randint(2, 20)

    sup_1 = random.randint(2, 4)
    sup_2 = random.randint(2, 4)

    eq = {
        f'x{sup_num(sup_1)}y + xy{sup_num(sup_2)}' : ((x ** sup_1) * y) + (x * (y ** sup_2)),
        f'x{sup_num(sup_1)} + y{sup_num(sup_2)}' : (x ** sup_1 ) + (y ** sup_2),
        f'x{sup_num(sup_2)}y + xy{sup_num(sup_1)}' : ((x ** sup_2) * y) + (x * (y ** sup_1)),
        f'x{sup_num(sup_1)} + xy{sup_num(sup_2)} + y{sup_num(sup_1)}' : (x** sup_1) + (x * (y ** sup_2)) + (y ** sup_1),
        f'x{sup_num(sup_1)}y + x{sup_num(sup_2)}y{sup_num(sup_1)}' : ((x ** sup_1) * y) + ((x ** sup_2) * (y ** sup_1))
    }

    key_eq = [f'x{sup_num(sup_1)}y + xy{sup_num(sup_2)}',
                f'x{sup_num(sup_1)} + y{sup_num(sup_2)}',
                f'x{sup_num(sup_2)}y + xy{sup_num(sup_1)}',
                f'x{sup_num(sup_1)} + xy{sup_num(sup_2)} + y{sup_num(sup_1)}',
                f'x{sup_num(sup_1)}y + x{sup_num(sup_2)}y{sup_num(sup_1)}'
                ]
    rand_eq_x, rand_eq_y = random.sample(key_eq, 2)

    question = f"If x : y = {x} : {y}, then solve for {rand_eq_x} : {rand_eq_y}"

    ans_x = eq[rand_eq_x]
    ans_y = eq[rand_eq_y]

    gcd = math.gcd(ans_x, ans_y)
    answer = f"{ans_x // gcd} : {ans_y // gcd}"
    return question, answer
