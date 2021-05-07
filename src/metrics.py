def precision(RR, RI):
    return RR / (RR + RI)


def recall(RR, NR):
    return RR / (RR + NR)


def F1(RR, RI, NR):
    P = precision(RR, RI)
    R = recall(RR, NR)

    return 2 / (1 / P + 1 / R)


def r_precision(RR, Total):
    return RR / Total


def fallout(RI, NI):
    return RI / (RI + NI)
