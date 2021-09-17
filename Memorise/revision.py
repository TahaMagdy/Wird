import sys
sys.path.append('/Users/taha/cs')
import pyquran as q

PARTS_COUNT = 6
my_suras = open('Hifz_taha.txt').readlines()

def print_list(list_):
    for s in list_:
        print(s)


get_sura = lambda name : q.quran.get_sura(q.quran.get_sura_number(name.strip()), basmalah=False)
def remove_spaces(sura):
    out = []
    for k in sura:
        out.append(k.replace(' ', ''))
    return out

# Drop any non alphabatical chars
compute_sura_length = lambda sura : len(''.join(remove_spaces(sura)))

# 1 * Preparing a suras_lengths = [(sura_name, sura_length)] # all suras (not partitioned yet)
suras_lengths = []
for sura_name in my_suras:
    sura_name     = sura_name.strip()
    sura_list_str = get_sura(sura_name)
    sura_len      = compute_sura_length(sura_list_str)
    suras_lengths.append((sura_name, sura_len))

# 2 * Sorting suras_lengths: [(sura_name, sura_length)]
suras_lengths.sort(key=lambda x:x[1], reverse=True)


def sum_groups_len(list_of_tuples):
    out = 0
    for _, length in list_of_tuples:
        out += length
    return out


def get_minimum_group_key(groups):
    minimum_length = float('inf')
    minimum_group_key = ''
    for key, value in groups.items():
        sum_group = sum_groups_len(value)
        if minimum_length > sum_group:
            minimum_length = sum_group
            minimum_group_key = key

    return minimum_group_key



# 3 * Computing the partitions
partitions = dict()
for i, name_length in enumerate(suras_lengths):
    name, length = name_length
    if len(partitions.keys()) < PARTS_COUNT:
        key = f'{i+1}:{PARTS_COUNT}'
        partitions[key] = [(name, length)]
        continue
    minimum_group = get_minimum_group_key(partitions)
    partitions[minimum_group].append((name, length))


def print_groups_sizes(partitions):
    for i, key_value in enumerate(partitions.items()):
        key, value = key_value
        print(key)
        print(value)
        print(f'{i+1}:{PARTS_COUNT} ', sum_groups_len(value))

def group_stat(partitions):
    for i, key_value in enumerate(partitions.items()):
        key, value = key_value
        print('\n\n')
        print(f'{key} الحزب')
        print('-'*9)
        for soura, size in value:
            print(soura, size)


group_stat(partitions)
# print('-'*10)
# print_groups_sizes(groups)
