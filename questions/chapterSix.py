import random



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
q, o, a = mof_4()
print(q, o, a)