import operator
from functools import reduce
from proba_distributor import ProbaDistributor

p_spell_error = 1. / 20.


def datafile(name, sep='\t'):
    """Reads key,value pairs from file."""
    with open(name, 'r') as file:
        # file = open(name)
        for line in file:
            yield line.split(sep)


def product(nums):
    """Returns the product of a sequence of numbers."""
    return reduce(operator.mul, nums, 1)


def pedit(edit, p: ProbaDistributor, spell_error: float):
    # TODO: According pg 234, this is the noisy model P(w|c). Need to verify.

    """The probability of an edit; can be '' or 'a|b' or 'a|b+c|d'."""

    if edit == '':
        return 1. - spell_error

    return p_spell_error * product(p(e) for e in edit.split('+'))
