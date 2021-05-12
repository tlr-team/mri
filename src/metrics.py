def precision(RR, RI):
    return RR / (RR + RI) if (RR + RI) != 0 else 0


def recall(RR, NR):
    return RR / (RR + NR) if (RR + NR) != 0 else 0


def F1(RR, RI, NR):
    P = precision(RR, RI) 
    R = recall(RR, NR)

    IP = 1 / P if P != 0 else 0
    IR = 1/ R if R != 0 else 0

    return 2 / (IP + IR) if (IP + IR) != 0 else 0


def r_precision(RR, RI):
    return RR / (RR + RI) if (RR + RI) != 0 else 0


def fallout(RI, NI):
    return RI / (RI + NI) if (RI + NI) != 0 else 0
