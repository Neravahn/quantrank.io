import random
import math



def mof_1():
    amt = random.randint(2000, 5000)
    yrs = random.randint(2, 8)
    rate = random.randint(12, 25)

    question = f"S.I on {amt} for {yrs}yrs at {rate}% per annum is ?"
    answer = (amt * rate * yrs) // 100

    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(2000, 5000)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer



def mof_2():
    principal = random.randint(2000, 5000)
    time = random.randint(2, 8)
    rate = random.randint(12, 25)
    interest = (principal * rate * time )// 100
    question = f"P = {principal}, T = {time}, I = {interest}, then per annum R will be"
    answer = rate

    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(12, 25)
        if option not in options or option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer



def mof_3():
    principal = random.randint(2000, 5000)
    time = random.randint(2, 8)
    rate = random.randint(12, 25)
    amount = principal + ((principal * rate * time) // 100 )



    question = f'P = {principal}, A = {amount}, T = {time}. Rate percent per annum simple interest will be:'
    answer = rate
    
    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(12, 25)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer



def mof_4():
    principal = random.randint(2000, 5000)
    rate = random.randint(12, 25)
    time = random.randint(2, 8)
    interest = (principal * rate * time) // 100

    question = f"P = {principal}, I = {interest}, R = {rate}% S.I.The numbers of years T will be"
    answer = time

    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(2, 8)
        if options not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_5():
    principal = random.randint(2000, 5000)
    time = 1
    rate = random.randint(12, 25)

    interest = (principal * time * (rate // 12)) // (12 * 100 )

    question = f"The sum required to earn a monthly interest of {interest} at {rate}% per annum SI"
    answer = principal

    options = []
    options.append(answer)
    while len(options)< 4:
        option = random.randint(2000, 5000)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_6():
    principal = random.randint(2000, 5000)
    rate = random.randint(12, 25)
    yrs_1 = random.randint(2, 8)
    yrs_2 = yrs_1 + random.randint(2, 5)
    amt_1 = (principal * rate * yrs_1) // 100
    amt_2 = (principal * rate * yrs_2) // 100
    

    question = f"The sum of money amount to {amt_1} in {yrs_1} yrs and {amt_2} in {yrs_2} yrs the principal and rate of interest are"
    answer = f"{principal}, {rate}% pa"

    options =  []
    options.append(answer)
    while len(options) < 4:
        option_p = random.randint(2000, 5000)
        option_r = random.randint(12, 25)
        option = f"{option_p}, {option_r}5 pa"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer



#============CI================
def mof_7():
    principal = random.randint(2000, 5000)
    time = random.randint(2, 8)
    rate = random.randint(12, 25)

    amt = principal * (1 +( rate / 100)) ** time 
    ci = amt - principal

    amt = round(amt)
    ci = round(ci)


    question = f"P = {principal}, R = {rate}, T = {time}, the amount and C.I is "
    answer = f"{amt}, {ci}"

    options = []
    options.append(answer)
    while len(options) < 4:
        option_amt = random.randint(5000, 50000)
        option_ci = random.randint(2000, 20000)

        option = f"{option_amt}, {option_ci}"
        if option not in options and option != answer and option_amt > option_ci:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer





def mof_8():
    principal = random.randint(500, 5000)
    time = random.randint(2, 50)
    rate = random.randint(12, 25)

    amt = principal* ( 1 + (rate / 100)) ** time

    question = f"{principal} will become after {time} at {rate}% per annum"
    answer = round(amt)

    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(2000, 300000)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer



def mof_9():
    rate = random.randint(2, 25)
    question = f"The effective rate of interest to a nominal rate {rate} % pa payable in half year will be"
    answer = round(((1 + rate / 200) ** 2 - 1) * 100 , 2)


    options = []
    options.append(answer)
    while len(options) < 4:
        option_rate = random.randint(2, 25)
        option = round(((1 + option_rate / 200) ** 2 - 1) * 100 , 2)

        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer





def mof_10():

    cost = random.randint(50000, 500000)
    scrap = random.randint(10000, 50000)
    rate = random.randint(12, 25)
    question = f"A machine is depreciated at a rate of  {rate}% on reducing balance. The original cost of the machine was {cost}, the ultimate scrap value is {scrap}, the effective life of the machine is"
    
    right = scrap / cost
    left = 1 - (rate / 100)
    time = math.log(right) / math.log(left)
    answer = f"{round(time, 2)} yrs"

    options = []
    options.append(answer)
    while len(options) < 4:
        option = round(random.uniform(10, 50), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer
q, a = mof_10()
print(q, a)

