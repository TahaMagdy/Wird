import sys
sys.path.append('/Users/taha/cs')

import pyquran as q
import re

quran_one_str = q.quran.retrieve_qruan_as_one_string()
quran_one_str = re.sub(r'\s', '', quran_one_str)

print(len(quran_one_str))


def remove_spaces(sura):
    out = []
    for k in sura:
        out.append(k.replace(' ', ''))
    return out

my_suras = open('list_me.txt').readlines()
get_sura = lambda name : q.quran.get_sura(q.quran.get_sura_number(name.strip()), basmalah=False)
# Drop any non alphabatical chars
compute_sura_length = lambda sura : len(''.join(remove_spaces(sura)))

suras_lengths = []
for sura_name in my_suras:
    sura_name = sura_name.strip()
    sura_list_str = get_sura(sura_name)
    sura_len = compute_sura_length(sura_list_str)
    suras_lengths.append((sura_name,sura_len))

memorized_size = 0
for sura_name, sura_size in suras_lengths:
    memorized_size += sura_size

quran_size = len(quran_one_str)

print(memorized_size/quran_size)