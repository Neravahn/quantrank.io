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
        if option not in options and option != answer:
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
        option = f"{round(random.uniform(10, 50), 2)} yrs"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_11():
    principal = random.randint(20000, 50000)
    time = random.randint(2, 15)
    rate = random.randint(12, 25)
    amt = round(principal * (1 +( rate / 200)) ** (2 * time))


    question = f"If A = {amt}, n = {time} years,  R = {rate} % per annum compound interest payable half yearly, then principal (P) is"
    answer = principal
    options = []
    options.append(answer)
    while len(options) < 4:
        option = random.randint(20000, 50000)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer



def mof_12():
    rate1 = random.randint(2, 8)
    rate2 = random.randint(10,50)

    time = math.log((rate2 + 100) / 100 ) / math.log(1 + (rate1/100))


    question = f"""The population of a town increases every year by {rate1}% of the population at the begining of that year. The number
    of year by which the total increases of population be {rate2}% is"""
    answer = f"{round(time, 2)} yrs"

    options = []
    options.append(answer)
    while len(options)< 4:
        option = f"{round(random.uniform(10, 50), 2)} yrs"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_13():
    principal = random.randint(2000, 5000)
    time = random.randint(2, 8)
    rate = random.randint(12, 25)

    SI = (principal * rate * time) // 100
    CI = principal * ((1 + (rate / 100)) ** time)

    diff = round(abs(SI - CI))

    question = f"The diffrence between C.I and S.I on a certain sum of money invested for {time} yrs at {rate}% per annum is {diff}. The principal is"
    answer = principal
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





def mof_14():
    cost = random.randint(5000, 50000)
    rate = random.randint(12, 25)
    time = random.randint(5, 15)

    scrap_val = cost * ((1 - rate / 100) ** time)
    question = f"The useful life of a machine is estimated to be {time} yrs and cost {cost}. Rate of depreciation is {rate}% p.a. The scrap value at the end of its life is"

    answer = round(scrap_val)

    options = []
    options.append(answer)
    while len(options)< 4:
        option = random.randint(1000, 9000)
        if option not in options and answer != option :
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_15():
    rate = random.randint(12, 25)

    effective_rate = (((1 + rate / 400) ** 4) - 1) * 100
    question = f"The effective rate of interest corresponding to nominal rate of {rate}% p.a convertible quaterly is"
    answer = f"{round(effective_rate, 2)}"

    options = []
    options.append(answer)
    while len(options) < 4:
        option = round(random.uniform(15, 40), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    

    random.shuffle(options)
    return question, options, answer




def mof_16():
    people = random.randint(2000, 5000)

    rate_d = round(random.uniform(12, 25), 2)
    rate_b = round(rate_d + random.uniform(5, 10), 2)
    
    effective_rate =( rate_b - rate_d) / people

    time = math.log((2 * people) / people)  / math.log(1 + (effective_rate)) 

    question = f"""The annual birth and death rates per {people} are {rate_b} and {rate_d} respectively. The number of years in which the population will be doubled
    assuming there is no immigration or emigration"""
    answer = f"{round(time, 2)} yrs"

    options = []
    options.append(answer)
    while len(options) < 4:
        option = f"{round(random.uniform(300, 600), 2)} yrs"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer




def mof_17():
    amt = random.randint(2000, 5000)
    time = random.randint(2, 8)
    rate = random.randint(12, 25)

    present_val = amt * ((1 - (1 + rate / 100) ** (- time)) / (rate / 100))
    question = f"The present value of an annuity of {amt} for {time} at {rate}% p.a C.I is"
    answer = round(present_val, 2)

    options = []
    options.append(answer)
    while len(options) < 4:
        option = round(random.uniform(3000, 5000), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer



def mof_18():
    amt = random.randint(200, 900)
    time = random.randint(2, 15)
    rate = round(random.uniform(2, 9), 2)

    fv = ((((1 + (rate / 100)) ** time) - 1) / (rate / 100)) * amt
    question= f"The amount of annuity certain of {amt} for {time} years at {rate}% p.a C.I is"
    answer = round(fv, 2 )


    options = []
    options.append(answer)
    while len(options) < 4:
        option = round(random.uniform(2000, 7000), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue
    
    random.shuffle(options)
    return question, options, answer




def mof_19():
    amt = random.randint(5000, 50000)
    rate = random.randint(12, 25)
    inst = random.randint(15, 50)
    inst_amt = amt * (rate /100) / (1 - (1 + rate / 100) ** (- inst))

    question = f"A loan of {amt} is to be paid back in {inst} equal installments. The amount of each installments to cover the principal at {rate}% p.a C.I is"
    answer = round(inst_amt, 2)

    options = []
    options.append(answer)
    while len(options) < 4:
        option  = round(random.uniform(5000, 9000), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer




def mof_20():
    amt = random.randint(20000, 50000)
    rate = random.randint(12, 25)
    inst = ((amt * rate) / 100) + random.randint(100, 5000)


    r = rate / 100 
    time = math.log(inst / (inst - amt * r)) / math.log(1 + r)

    question = f"A company borrows {amt} on condition to repay it with compound interest at {rate} % p.a by annual installments of {inst} the number of years by which the debts will be cleared is"
    answer = f"{round(time, 2)} yrs"

    options = []
    options.append(answer)
    while len(options) < 4:
        option = f"{round(random.uniform(3, 15), 2)} yrs"
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer





def mof_21():
    principal = random.randint(4000, 15000)
    rate = random.randint(12, 25)
    time = random.randint(2, 8)


    amt = principal * ((1 + rate / 100) ** time)
    interest = amt - principal


    question = f"Mr. X borrowed {principal} at {rate}% p.a C.I. At the end of {time} years, the money was repaid along with the interest acccrued. The amount of interest paid by him is"
    answer = round( interest, 2)

    options = []
    options.append(answer)
    while len(options) < 4:
        option = round(random.uniform(2000, 15000), 2)
        if option not in options and option != answer:
            options.append(option)
        else:
            continue

    random.shuffle(options)
    return question, options, answer
q, o, a = mof_21()
print(q,  o, a)

