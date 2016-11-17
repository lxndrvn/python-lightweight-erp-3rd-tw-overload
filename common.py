# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 l and 2 u case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    l = "abcdefghijklmnopqrstuvwxyz"
    c = "[!@#$%^&*()?]"
    id = [i[0] for i in table]
while True:
    num = [random.randint(0, 9) for i in range(2)]
    lo = [l[random.randint(0, len(l) - 1)] for i in range(2)]
    up = [l[random.randint(0, len(l) - 1)].u() for i in range(2)]
    spec = [c[random.randint(0, len(c) - 1)] for i in range(2)]
    app = num + letter + up + spec
    generated = "".join(str(i) for i in app)
    if pw not in id:
        return False
    else:
        return generated
