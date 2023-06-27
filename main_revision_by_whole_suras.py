import sys
sys.path.append('/Users/tahamagdy/MacBook-13/cs')
sys.path.append('/Users/tahamagdy/MacBook-13/cs/quran')

import pyquran as q
import MemorizedQuran

def print_list(list_):
    for s in list_:
        print(s)

days = {
    0:'السبت'
  , 1:'الأحد'
  , 2:'الإثنين'
  , 3:'الثلاثاء'
  , 4:'الأربعاء'
  , 5:'الخميس'
  , 6:'الجمعة'
}


my_suras = [sura for sura, memo_state in MemorizedQuran.quran.items() if memo_state == MemorizedQuran.YES]



get_sura = lambda name : q.quran.get_sura(q.quran.get_sura_number(name.strip()), basmalah=False)
def remove_spaces(sura):
    out = []
    for k in sura:
        out.append(k.replace(' ', ''))
    return out

# Drop any non alphabatical chars
compute_sura_length = lambda sura : len(''.join(remove_spaces(sura)))

# TODO: Name the dicationary `revision` and change the rest accordingly
# * Preparing a suras_lengths = [(sura_name, sura_length)]
suras_lengths = []
for sura_name in my_suras:
    sura_name = sura_name.strip()
    sura_list_str = get_sura(sura_name)
    sura_len = compute_sura_length(sura_list_str)
    suras_lengths.append((sura_name,sura_len))


#print_list(suras_lengths)


# * Sorting suras_lengths: [(sura_name, sura_length)]
#suras_lengths = suras_lengths[:-37] # exclude the last 37 sura from Annb'a to the end
sura_length = suras_lengths.sort(key=lambda x:x[1], reverse=True)
groups = dict()
i = 1


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



# Computing the Groups
GROUPS = 7
for length, name in suras_lengths:
    print(length)
    if len(groups.keys()) < GROUPS:
        groups['Day ' + str(i)] = [(length, name)]
        i += 1
        continue
    minimum_group = get_minimum_group_key(groups)
    groups[minimum_group].append((length, name))

def group_stat(grous):
    for key, value in grous.items():
        print(f'{key}: ', sum_groups_len(value))

def group_stat(grous):
    i = 0
    for _, value in grous.items():
        print('\n\n')
        print(f'{days[i % 7]}')
        print('-'*7)
        i += 1
        for soura, size in value:
            #print(size, soura)
            print(soura, size)

#pprint(groups)
group_stat(groups)