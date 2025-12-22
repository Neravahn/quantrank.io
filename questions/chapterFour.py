import random
from fractions import Fraction
import math

def equation_1():
    const1 = random.randint(2, 9)
    const2 = random.randint(2, 9)

    while True:
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        if x != y and x + y != 0 :
            break

    eq_templates = [
        f"(x / {const1}) + (y / {const2})",
        f"({const1}x + {const2}y)",
        f"({const1}x - y)",
        f"(x + y) / (x - y)",
        f"x - {const1}y",
        f"x + {const1}y",
        f"({const1} / (x + y)) + ({const2} / (x - y))",
    ]

    sol = {
        f"(x / {const1}) + (y / {const2})": Fraction(x, const1) + Fraction(y, const2),
        f"({const1}x + {const2}y)": Fraction(const1*x + const2*y),
        f"({const1}x - y)": Fraction(const1*x - y),
        f"(x + y) / (x - y)" :Fraction((x + y), (x - y)),
        f"x - {const1}y": Fraction(x - const1*y),
        f"x + {const1}y": Fraction(x + const1*y),
        f"({const1} / (x + y)) + ({const2} / (x - y))": Fraction(const1, (x + y)) + Fraction(const2, (x - y))
    }

    lhs1, lhs2 = random.sample(eq_templates, 2)

    rhs1 = round(sol[lhs1], 2)
    rhs2 = round(sol[lhs2], 2)


    templates = [
        f"The solution set of equations {lhs1} = {rhs1}, {lhs2} = {rhs2} is",
        f"The values of x and y stisfying the equation {lhs1} = {rhs1}, {lhs2} = {rhs2} are given by the pair", 
        f"Solve for x and y: {lhs1} = {rhs1} and {lhs2} = {rhs2}",
        f"The pair satifying the equations {lhs1} = {rhs1}, {lhs2} = {rhs2} are given by",
        f"The simultaneous equaitions {lhs1} = {rhs1}, {lhs2} = {rhs2} have solutions given by"
    ]  

    question = random.choice(templates)
    answer = f"(x={x}, y={y})"
    options = []
    options.append(answer)
    while len(options) < 4:
        option_x = random.randint(2, 9)
        option_y = random.randint(2, 9)

        option = f"(x={option_x}, y={option_y})"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue


    random.shuffle(options)

    return question, options, answer





def equation_2():
    const1 = random.randint(2, 20)
    const2 = random.randint(2, 20)
    const3 = random.randint(2, 20)

    while True:
        x = random.randint(2, 20)
        y = random.randint(2, 20)
        z = random.randint(2, 20)

        if x!=y!=z:
            break

    eq_templates = [
        "xy / (x + y)",
        "yz / (y + z)",
        "xz / (x + z)",
        f"{const1}x + {const2}y + {const3}z",
        f"{const1}x + {const2}y - {const3}z",
        f"{const1}x - {const2}y + {const3}z",
        f"{const1}(x + y) + 2z",
        f"{const1}x - {const2}(y + z)",
        f"x + {const1}(x + y - z)"
    ]

    sol = {
        "xy / (x + y)": Fraction((x * y), (x + y)),
        "yz / (y + z)": Fraction((y * z), (y + z)),
        "xz / (x + z)": Fraction((x * z),  (x + z)),
        f"{const1}x + {const2}y + {const3}z": (const1 * x) + (const2 * y) + (const3 * z),
        f"{const1}x + {const2}y - {const3}z": (const1 * x) + (const2 * y) - (const3 * z),
        f"{const1}x - {const2}y + {const3}z": (const1 * x) - (const2 * y) + (const3 * z),
        f"{const1}(x + y) + 2z" :(const1 * ( x + y)) + (2 * z),
        f"{const1}x - {const2}(y + z)": (const1 * x) - (const2 * (y + z)),
        f"x + {const1}(x + y - z)": x + (const1 * (x + y - z))
    }

    

    rand_1, rand_2= random.sample(eq_templates, 2)
    sol_1 = round(sol[rand_1], 2)
    sol_2 = round(sol[rand_2], 2)
    question = f"{rand_1} = {sol_1}, {rand_2} = {sol_2}"

    answer = f"(x = {x}, y = {y}, z = {z})"
    options = []
    options.append(answer)
    while len(options) < 4:
        option_x = random.randint(2, 20)
        option_y = random.randint(2, 20)
        option_z = random.randint(2, 20)
        option = f"(x = {option_x}, y = {option_y}, z = {option_z})"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer






def equation_3():
    num_val = []
    while len(num_val) < 2:
        z = random.randint(2, 20)
        if z not in num_val:
            num_val.append(z)
        else:
            continue

    x = num_val[0]
    y = num_val[1]
    while True :
        mul = random.randint(40, 100)
        real_x = x * mul
        real_y = y * mul

        save = random.randint(10, min(real_x, real_y) - 1)

        spend_x = real_x - save
        spend_y = real_y - save

        gcd = math.gcd(spend_x, spend_y)
        if gcd:
            p = spend_x // gcd
            q = spend_y // gcd
            break
        else:
            continue


    question = f"Monthly income of two persons are in the ratio {x} : {y} and their monthly expenses are in the ratio {p} : {q}. If each saves {save} per month find their monthly incomes"

    answer = f"({real_x}, {real_y})"

    options = []
    options.append(answer)
    while len(options) < 4:
        x = random.randint(80, 2000)
        y = random.randint(80, 2000)
        if x != y:
            option = f"({x}, {y})"
            if option not in options:
                options.append(option)
            else:
                continue
        else:
            continue

    
    random.shuffle(options)
    
    return question, options, answer
q, o, a = equation_3()
print(q, o, a)