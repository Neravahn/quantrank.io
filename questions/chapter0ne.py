import random
import math
from sub_supScript import sub_num, sub_text, sup_num, sup_text

def ratio_1():
    ear = []
    while len(ear) < 2:
        z = random.randint(2, 20)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    x = random.randint(1, 20)
    c = a_s * x

    question = f"The ratio of two quantities is {a_s} : {b_s}. If the antecedent is {c}, the consequent is ?"
    answer = b_s * x

    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(2, 20)
        if option not in options and option != answer:
            options.append(option)
        else :
            continue

    random.shuffle(options)
    return question, options, answer





def ratio_2():
    ear = []
    while len(ear) < 2:
        z = random.randint(2, 20)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)

    a_s, b_s = a//gcd, b//gcd

    question = f"The duplicate ratio of {a_s} : {b_s} is ?"
    answer = f"{a_s ** 2} : {b_s **2}"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(2, 20)
            if z not in ear:
                ear.append(z)
            else:
                continue
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)
        option = f"{(option_x // gcd) ** 2} : {(option_y // gcd) ** 2}"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer








def ratio_3():
    ear = []
    while len(ear) < 2:
        z = random.randint(2, 9)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b =ear[1]
    gcd = math.gcd(a, b)
    a_s, b_s = a // gcd, b // gcd

    a_s_squared, b_s_squared = a_s ** 2, b_s ** 2

    question = f"The sub-duplicate ratio of {a_s_squared} : {b_s_squared} is ?"
    answer = f"{a_s} : {b_s}"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(2, 9)
            if z not in ear:
                ear.append(z)
            else:
                continue
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)
        option = f'{option_x // gcd} : {option_y // gcd}'
        if option not in options and option != answer:
            options.append(option)


    random.shuffle(options)
    return question, options, answer






def ratio_4():
    ear =[]
    while len(ear) < 2:
        z = random.randint(2, 10)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)
    a_s, b_s = a//gcd, b//gcd
    
    question = f"The triplicate ratio of {a_s} : {b_s} is ?"
    answer = f"{a_s ** 3} : {b_s ** 3}"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear =[]
        while len(ear) < 2:
            z = random.randint(2, 10)
            if z not in ear:
                ear.append(z)
            else:
                continue
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)
        option = f"{(option_x // gcd) ** 3} : {(option_y //gcd) ** 3}"
        if option not in options and option != answer:
            options.append(option)

    random.shuffle(options)
    return question, options, answer






def ratio_5():
    ear =[]
    while len(ear) < 2:
        z = random.randint(2, 9)
        if z not in ear:
            ear.append(z)
        else:
            continue
        
    a= ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)

    a_s, b_s = a // gcd, b //gcd

    question = f"The sub-triplicate ratio of {a_s ** 3} : {b_s ** 3} is ?"
    answer = f"{a_s} : {b_s}"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear =[]
        while len(ear) < 2:
            z = random.randint(2, 9)
            if z not in ear:
                ear.append(z)
            else:
                continue
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)
        option = f"{option_x // gcd} : {option_y // gcd}"
        if option not in options and option != answer:
            options.append(option)

    random.shuffle(options)
    return question, options, answer






def ratio_6():
    ear =[]
    while len(ear) < 4:
        z = random.randint(2, 10)
        if z not in ear:
            ear.append(z)
        else:
            continue
    
    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)
    a_s = a // gcd
    b_s = b//gcd

    c = ear[2]
    d = ear[3]
    gcd = math.gcd(c, d)
    c_s = c//gcd
    d_s = d//gcd

    question = f"The ratio compounded of {a_s} : {b_s} and the duplicate ratio of {c_s} : {d_s} is"
    f_a = (a_s) * (c_s ** 2)
    f_b = (b_s) * (d_s ** 2)
    f_g = math.gcd(f_a, f_b)
    answer = f"{f_a // f_g} : {f_b // f_g}"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear =[]
        while len(ear) < 4:
            z = random.randint(2, 10)
            if z not in ear:
                ear.append(z)
            else:
                continue
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)

        option_r = ear[2]
        option_s = ear[3]
        gcd_2 = math.gcd(option_r, option_s)
        option = f"{(option_x // gcd) * ((option_r // gcd_2) ** 2)} : {(option_y // gcd) * ((option_s // gcd_2) ** 2)}"
        if option not in options and option != answer:
            options.append(option)

    random.shuffle(options)
    return question, options, answer






def ratio_7():
    ear = []
    while len(ear) < 8:
        z = random.randint(2, 10)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b = ear[1]
    gcd= math.gcd(a, b)
    a_s = a // gcd
    b_s = b// gcd


    c = ear[2]
    d = ear[3]
    gcd = math.gcd(c, d)
    c_s = c// gcd
    d_s = d//gcd


    e = ear[4]
    f = ear[5]
    gcd = math.gcd(e, f)
    e_s = e // gcd
    f_s = f // gcd

    g = ear[6]
    h = ear[7]
    gcd = math.gcd(g, h)
    g_s = g//gcd
    h_s = h// gcd

    question = f"The ratio compunded of {a_s} : {b_s}, the duplicate ratio of {c_s} : {d_s} the triplicate ratio of {e_s} : {f_s} and {g_s} : {h_s}"
    f_a = (a_s) * (c_s ** 2) * (e_s ** 3) * (g_s)
    f_b = (b_s) * (d_s ** 2) * (f_s ** 3) * (h_s)
    gcd = math.gcd(f_a, f_b)
    answer = f"{f_a // gcd} : {f_b // gcd}"

    options = []
    options.append(answer)
    while len(options) < 4:
        option_list = []
        while len(option_list) < 8:
            a = random.randint(2, 10)
            if a not in options and a != answer:
                option_list.append(a)
            else:
                continue
        option_x = (option_list[0]) * (option_list[1] ** 2) * (option_list[2] ** 3) * (option_list[3])
        option_y = (option_list[4]) * (option_list[5] ** 2) * (option_list[6] ** 3) * (option_list[7])
        gcd = math.gcd(option_x, option_y)
        option = f"{option_x // gcd} : {option_y // gcd}"
        if option not in options:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer






def ratio_8():
    ear = []
    while len(ear) < 2:
        z = random.randint(3, 10)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a_s = ear[0]
    b_s = ear[1]
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

    options = []
    options.append(answer)
    while len(options) < 4:
        list = []
        while len(list) < 2:
            p = random.randint(3, 10)
            if p not in list:
                list.append(p)
            else:
                continue

        const = random.randint(4, 8)
        option_x = list[0] * const
        option_y = list[1] * const
        option = f"({option_x}, {option_y})"
        if option not in options:
            options.append(option)

    random.shuffle(options)
    return question, options, answer






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
        ear = []
        while len(ear) < 3:
            z = random.randint(2, 50)
            if z not in ear:
                ear.append(z)
            else:
                continue

        if sum(ear) == div_angle:
            break
        else:
            continue

    a =ear[0]
    b = ear[1]
    c = ear[2]

    question = f"The angles of a triangle are in ratio {a} : {b} : {c}. Find the angles"
    answer = f"({a * x}, {b * x}, {c * x})"

    options = []
    options.append(answer)
    while len(options) < 4:
        list = []
        while len(list) < 3:
            p = random.randint(40, 100)
            if p not in list:
                list.append(p)
            else:
                continue

            if len(list) == 3 and sum(list) == 180:
                break
            else:
                continue

        num_1 = list[0]
        num_2 = list[1]
        num_3 = list[2]

        option = f"({num_1}, {num_2}, {num_3})"
        if option not in options:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer






def ratio_10():
    ear = []
    while len(ear) < 2:
        z = random.randint(2, 20)
        if z not in ear:
            ear.append(z)
        else:
            continue
    
    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)

    x = random.randint(20, 50)

    total_amt = (a * x) + (b * x)

    question = f"Division of {total_amt}$ between X and Y is in ratio {a // gcd} : {b // gcd}. X and Y would get ?"
    answer = f"({a * x}, {b * x})"

    options = []
    options.append(answer)
    while len(options)< 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(40, 1000) #<--- THIS WAL LOWEST TO LOWER MUL AND HIGHEST TO HIGHEST
            if z not in ear:
                ear.append(z)
            else:
                continue
        
        option_x = ear[0]
        option_y = ear[1]

        option = f"({option_x}, {option_y})"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer






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
    ear = []
    while len(ear) < 2:
        z = random.randint(3, 15)
        if z not in ear:
            ear.append(z)
        else:
            continue

    a = ear[0]
    b = ear[1]
    gcd = math.gcd(a, b)

    x = random.randint(20, 90)
    
    d = abs((a*x) - (b*x))

    question = f"The ratio of two numbers is {a // gcd} : {b // gcd}, their diffrence is {d}. Find the numbers"
    answer = f"({a*x}, {b*x})"

    options = []
    options.append(answer)
    while len(options) < 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(60, 1350)
            if z not in ear:
                ear.append(z)
            else:
                continue
        
        option = f"({ear[0], ear[1]})"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer






def ratio_13():
    ear = []
    while len(ear) < 4:
        z = random.randint(3, 20)
        if z not in ear:
            ear.append(z)
        else:
            continue
    a = ear[0]
    b = ear[1]
    c = ear[2]
    d = ear[3]


    question = f"P, Q and R are three cities. The ratio of average temprature between P and Q is {a} : {b} and that between P and R is {c} : {d}. The ratio between temprature of Q and R is ?"
    gcd = math.gcd((a *d), (b * c))
    z = (a * d) // gcd
    y = (b * c) // gcd

    answer = f"{y} : {z}"
    
    options = []
    options.append(answer)
    while len(options) < 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(60, 400)
            if z not in ear:
                ear.append(z)
            else:
                continue

        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)

        option = f"{option_x // gcd} : {option_y // gcd}"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question , options, answer







def ratio_14():
    ear = []
    while len(ear) < 2:
        z = random.randint(2, 20)
        if z not in ear:
            ear.append(z)
        else:
            continue
    
    x = ear[0]
    y = ear[1]
    gcd = math.gcd(x, y)
    x = x // gcd
    y = y // gcd


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

    options = []
    options.append(answer)
    while len(options) < 4:
        ear = []
        while len(ear) < 2:
            z = random.randint(300, 2000)
            if z not in ear:
                ear.append(z)
            else:
                continue
        
        option_x = ear[0]
        option_y = ear[1]
        gcd = math.gcd(option_x, option_y)

        option = f"{option_x // gcd} : {option_y // gcd}"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options) 
    return question, options, answer






def ratio_15():
    ear = []
    while len(ear) < 4:
        z = random.randint(2, 15)
        if z not in ear:
            ear.append(z)
        else:
            continue
        
    p_s = ear[0]
    q_s = ear[1]
    gcd_1 = math.gcd(p_s, q_s)
    p = p_s // gcd_1
    q = q_s // gcd_1

    x_s = ear[2]
    y_s = ear[3]
    gcd_2 = math.gcd(x_s, y_s)
    x = x_s // gcd_2
    y = y_s // gcd_2

    mul_1 = random.randint(2, 10)
    mul_2 = random.randint(2, 10)
    sub_1 = random.randint(2, 4)
    sub_2 = random.randint(2, 4)

    eq = {
            f"{mul_1}px + {mul_2}qy" : (mul_1 * p * x) + (mul_2 * q * y),
            f"{mul_1}pq - {mul_2}xy" : (mul_1 * p * q) - (mul_2 * x * y),
            f"p{sup_num(sub_1)}y + {mul_2}q x{sup_num(sub_2)}" : ((p ** sub_1) * y) + (mul_2 * q * (x ** sub_2)),
            f"x{sup_num(sub_2)}y{sup_num(sub_2)} + {mul_1}pq" : ((x ** sub_2) * (y ** sub_2)) + (mul_1 * p * q),
            f"{mul_1}q x{sup_num(sub_1)} + p{sup_num(sub_2)} {mul_2}y" : (mul_1 * q * (x ** sub_1)) + ((p ** sub_2) * mul_2 * y),
        }

    eq_key = [
        f"{mul_1}px + {mul_2}qy",
        f"{mul_1}pq - {mul_2}xy",
        f"p{sup_num(sub_1)}y + {mul_2}q x{sup_num(sub_2)}",
        f"x{sup_num(sub_2)}y{sup_num(sub_2)} + {mul_1}pq",
        f"{mul_1}q x{sup_num(sub_1)} + p{sup_num(sub_2)} {mul_2}y"
    ]

    rand_eq_x, rand_eq_y = random.sample(eq_key, 2)

    question = f"If p : q = {p} : {q} and x : y = {x } : {y}, then the value of {rand_eq_x} : {rand_eq_y}"
    sol_x = eq[rand_eq_x]
    sol_y = eq[rand_eq_y]
    gcd = math.gcd(sol_x, sol_y)

    answer = f"{sol_x // gcd} : {sol_y // gcd}"

    options = []
    options.append(answer)
    while len(options) < 4:
        num_val = []
        while len(num_val) < 2:
            z = random.randint(50, 300)
            if z not in num_val:
                num_val.append(z)
            else:
                continue
        
        option_x = num_val[0]
        option_y = num_val[1]
        gcd = math.gcd(option_x, option_y)

        option = f"{option_x // gcd} : {option_y // gcd}"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer






def ratio_16():
    amt_ratio = []
    while len(amt_ratio) < 2:
        z = random.randint(2, 15)
        if z not in amt_ratio:
            amt_ratio.append(z)
        else:
            continue
    
    amt_const = random.randint(40, 100)
    ear_1 = amt_ratio[0]
    ear_2 = amt_ratio[1]
    gcd_1 = math.gcd(ear_1, ear_2)

    amt_1 = ear_1 * amt_const
    amt_2 = ear_2 * amt_const

    
    while True:
        save = random.randint(50, 100)
        spend_1 = amt_1 - save
        spend_2 = amt_2 - save
        gcd_2 = math.gcd(spend_1, spend_2)
        if gcd_2 is None:
            continue
        else:
            break
        
    question = f"Daily earning of two persons are in the ratio {ear_1 // gcd_1} : {ear_2 // gcd_1} and their daily expenses are in the ratio {spend_1 // gcd_2} : {spend_2 // gcd_2} if each save {save} per day, their daily earnings are? (round off if required)"
    answer = f"({amt_1}, {amt_2})"

    options = []
    options.append(answer)
    while len(options) < 4:
        num_val = []
        while len(num_val) < 2:
            z = random.randint(300, 1000)
            if z not in num_val:
                num_val.append(z)
            else:continue
        
        x = num_val[0]
        y = num_val[1]
        option = f"({x}, {y})"
        if option not in options and option != answer:
            options.append(option)
        else: 
            continue

    random.shuffle(options)
    return question, options, answer
q, o, a = ratio_16()
print(q, o, a)






def ratio_17():
    num_val = []
    while len(num_val) < 2:
        z = random.randint(2, 15)
        if z not in num_val:
            num_val.append(z)
        else:
            continue

    x_s = num_val[0]
    y_s = num_val[1]
    gcd = math.gcd(x_s, y_s)
    x = x_s // gcd
    y = y_s // gcd

    dist = random.randint(300, 800)
    hrs =  random.randint(3, 9)
    question = f"The ratio between the speeds of two trains is {x} : {y}. If the second train runs {dist} kms in {hrs}, the speed of the first train is? (rounhd off if necessary)"
    speed_2 = dist // hrs
    const = speed_2 // y
    answer = const * x

    options = []
    options.append(answer)
    while len(options) < 4:
        z = random.randint(20, 300)
        if x not in options and z != answer:
            options.append(z)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer
q, o, a = ratio_17()
print(q, o, a)
