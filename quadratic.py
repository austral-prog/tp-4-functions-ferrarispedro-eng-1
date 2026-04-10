def roots(a, b, c):
    
    disc = (b**2) - (4 * a * c)
    if disc < 0:
        return "( )"
    raiz = disc ** 0.5
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    if disc == 0:
        return "(" + str(round(x1, 1)) + ")"
    else:
        return "(" + str(round(x1, 1)) + ", " + str(round(x2, 1)) + ")"


def value_y(a, b, c, x):

    if a != 0 and b != 0 and c != 0:

        return (a * x ** 2) + (b * x) + (c)

    elif a != 0 and b != 0 and c == 0:

        return (a* x ** 2) + (b * x)

    elif a != 0 and b == 0 and c != 0:

        return (a * x ** 2) + (c)

    elif a != 0 and b == 0 and c == 0:

        return (a * x ** 2)

    elif a == 0 and b != 0 and c != 0:
        return (b * x) + (c)

    elif a == 0 and b != 0 and c == 0:
        return (b*x)

    elif a == 0 and b == 0 and c != 0:
        return (c)

    elif a == 0 and b == 0 and c == 0:
        return (0)


def to_string(a, b, c):
    terms = []
    if a != 0:
        terms.append(str(a) + " * X^2")
    if b != 0:
        terms.append(str(b) + " * X")
    if c != 0:
        terms.append(str(c))
    if not terms:
        return "f(x) = 0"
    return "f(x) = " + " + ".join(terms)


def derivation(a, b, c):
    terms = []
    if 2 * a != 0:
        terms.append(str(2 * a) + " * X")
    if b != 0:
        terms.append(str(b))
    if not terms:
        return "f'(x) = 0"
    return "f'(x) = " + " + ".join(terms)