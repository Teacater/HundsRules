levels = ["", "s", "p", "d", "f", "g"]


def get_cap(l):
    return ((l - 1) * 2 + 1) * 2


def get_m(l, max_l):
    return int(l - (max_l - 1) / 2)


def add_state(var):
    for i in range(len(var)):
        if var[i] < 4:
            var[i] += 1
            return True
        else:
            var[i] = 1
    return False


def get_all_states(n, l):
    generate = True
    states = []
    var = []
    for i in range((l - 1) * 2 + 1):
        var.append(1)
    states.append(var.copy())
    while generate:
        generate = add_state(var)
        if generate:
            states.append(var.copy())
    remove_states = []
    for i in states:
        for j in range(len(i)):
            if i[j] == 4:
                i[j] = -99
            elif i[j] == 3:
                i[j] = 0
            elif i[j] == 2:
                i[j] = 0.5
            else:
                i[j] = -0.5
        s = 0
        for j in range(len(i)):
            if i[j] == 0.5 or i[j] == -0.5:
                s += 1
            elif i[j] == 0:
                s += 2
        if s != n:
            remove_states.append(i)
    for i in remove_states:
        states.remove(i)
    new_states = []
    for i in states:
        ml = 0
        ms = 0
        for j in range(len(i)):
            if i[j] == 0.5 or i[j] == -0.5:
                ms += i[j]
                ml += get_m(j, len(i))
            elif i[j] == 0:
                ml += 2 * get_m(j, len(i))
        new_states.append({"state": i, "ml": ml, "ms": ms})
    return new_states


def generate_terms(n, l):
    states = get_all_states(n, l)
    max_ml = states[0]["ml"]
    for i in states:
        if i["ml"] > max_ml:
            max_ml = i["ml"]
    current_l = max_ml
    terms = []
    while current_l >= 0:
        local_states = []
        s = -100000000
        for i in states:
            if i["ml"] == current_l and i["ms"] > s:
                s = i["ms"]
        for i in range(-current_l, current_l + 1):
            for j in range(-int(2*s), int(2*s) + 1):
                for k in states:
                    if k["ml"] == i and int(2 * k["ms"]) == j:
                        local_states.append(k)
                        break
        for i in local_states:
            states.remove(i)
        J = []
        J.append(current_l + s)
        if abs(current_l - s) != current_l + s:
            J.append(abs(current_l - s))
        terms.append({"L": current_l, "S": s, "J": J, "states": local_states})
        current_l -= 1
    print("__________")
    print("Возможные термы:")
    for i in terms:
        t = i.copy()
        t["J"] = t["J"][0]
        print_term(t)
        if len(i["J"]) > 1:
            t["J"] = i["J"][1]
            print_term(t)

    return terms


def generate_general_term(terms):
    local_terms = []
    s = -1000
    for i in terms:
        if i["S"] > s:
            s = i["S"]
    for i in terms:
        if i["S"] == s:
            local_terms.append(i)
    s = -1000
    for i in local_terms:
        if i["L"] > s:
            s = i["L"]
    last_terms = []
    for i in local_terms:
        if i["L"] == s:
            last_terms.append(i)
    general_term = last_terms[0]
    count = 0
    s = 0
    for i in general_term["states"][0]["state"]:
        count += 1
        if i == 0.5 or i == -0.5:
            s += 1
        elif i == 0:
            s += 2
    if s >= count / 2:
        general_term["J"] = max(general_term["J"])
    else:
        general_term["J"] = min(general_term["J"])

    print("Основной терм:")
    print_term(general_term)


def print_term(term):
    print(str(int(term["S"] * 2 + 1)) + levels[term["L"] + 1].upper() + str(term["J"]))


def print_e_configuration(conf, last):
    print("Электронная конфигурация")
    for i in range(len(conf)):
        n, l = conf[i]
        if i == len(conf) - 1:
            max_cap = str(last)
        else:
            max_cap = str(get_cap(l))
        print(str(n) + levels[l] + "^" + max_cap, end=" ")
    print("")


def get_electron_configuration(n):
    s = n
    current_cap = 2
    current_n = 1
    current_l = 1
    conf = [(current_n, current_l)]
    start = 1
    while s > current_cap:
        s -= current_cap
        current_n += 1
        current_l -= 1
        if current_l < 1 or current_n < 1:
            current_n = 1
            start += 1
            current_l = start
            while current_l > current_n:
                current_n += 1
                current_l -= 1

        conf.append((current_n, current_l))
        current_cap = get_cap(current_l)

    return current_cap, s, conf