import sys
sys.path.append('..')

import pyquran as q
from pprint import pprint

my_suras = open('list_me.txt').readlines()

get_sura = lambda name : q.quran.get_sura(q.quran.get_sura_number(name.strip()), basmalah=False)
compute_sura_length = lambda sura : len(''.join(sura))

suras_lengths = []
for sura_name in my_suras:
    sura_name = sura_name.strip()
    sura_string = get_sura(sura_name)
    sura_len = compute_sura_length(sura_string)
    suras_lengths.append((sura_name,sura_len))


sura_length = suras_lengths.sort(key=lambda x:x[1], reverse=True)
groups = dict()
i = 1


def sum_lengths(list_of_tuples):
    out = 0
    for _, length in list_of_tuples:
        out += length
    return out


def get_minimum_group_key(groups):
    minimum_length = float('inf')
    minimum_group_key = ''
    for key, value in groups.items():
        sum_group = sum_lengths(value)
        if minimum_length > sum_group:
            minimum_length = sum_group
            minimum_group_key = key

    return minimum_group_key



# Computing the Groups
GROUPS = 7
for length, name in suras_lengths:
    if len(groups.keys()) < GROUPS:
        groups['group ' + str(i)] = [(length, name)]
        i += 1
        continue
    minimum_group = get_minimum_group_key(groups)
    groups[minimum_group].append((length, name))

pprint(groups)
def group_stat(grous):
    for key, value in grous.items():
        print(f'{key}: ', sum_lengths(value))

group_stat(groups)
