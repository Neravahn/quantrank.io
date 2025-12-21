import random

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
        f"(x / {const1}) + (y / {const2})": (x / const1) + (y / const2),
        f"({const1}x + {const2}y)": (const1 * x) + (const2 * y),
        f"({const1}x - y)": (const1 * x) - y,
        f"(x + y) / (x - y)" :(x + y) / (x - y),
        f"x - {const1}y" : x - (const1 * y),
        f"x + {const1}y": x + ( const1 * y),
        f"({const1} / (x + y)) + ({const2} / (x - y))": (const1 / (x + y)) + (const2 / (x - y))
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


q, o, a = equation_1()

print(q, o, a)