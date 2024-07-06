#!/bin/python3
from functools import reduce


def solve_chinese_remainder(mods, vals):
    """
    Solves a chinese remaindering task of the form:
        x % a = r
        x % b = u
        x % c = v
        ...

    Args:
        mods: The list of modulos. In the example, it would be [a, b, c, ...]
        vals: The list of values. In the example, it would be [r, u, v, ...]

    Returns:
        The value x
    """
    assert len(mods) == len(vals)

    sol = 0
    super_modulo = reduce(lambda acc, m: acc * m, mods)
    for m_i, a_i in zip(mods, vals):
        p = reduce(lambda acc, m: acc * m, [m for m in mods if m != m_i])
        sol += a_i * p * pow(p, -1, m_i)

    return sol % super_modulo
