""" How much should I revisie quran to finish my (memorized suras) in N days?
"""


import sys
sys.path.append('/Users/taha/cs')
sys.path.append('/Users/taha/cs/quran')
import pyquran as q
import math

import SuraNames


def get_memorized_sura_as_one_string(suras_names: list):
    ayat_one_list = []
    for sura_name in suras_names:
        sura_as_list = q.quran.get_sura(q.quran.get_sura_number(sura_name.strip()), basmalah=False)
        ayat_one_list += sura_as_list

    one_string = ' '.join(ayat_one_list)
    return one_string


get_sura_with_name = lambda name: q.quran.get_sura(q.quran.get_sura_number(name))


def count_arabic_letters(aya):
    x = 0
    for char in aya:
        if char in q.arabic.alphabet:
            x += 1
    return x

def print_suras_if_they_are_less_than_9(partition_suras):
    if len(partition_suras) <= 9:
        print(' - '.join(partition_suras))

def print_hizb(memorized_sura_names, NUMBER_PARTITIONS=7):

    memorized_string = get_memorized_sura_as_one_string(memorized_sura_names)

    len_memorized_quran = count_arabic_letters(memorized_string)
    len_parition        = math.floor(len_memorized_quran / NUMBER_PARTITIONS)

    print('>> ', len_parition, len_memorized_quran, len_memorized_quran / len_parition)
    print()

    candidate_PN       = 0
    test_len_memorised = 0
    len_TEST           = 0
    partition_count    = 1
    partition_suras    = []
    hizb_begins_at     = 'أول القرءان'

    for sura_name in memorized_sura_names:
        sura = get_sura_with_name(sura_name)

        for i, aya in enumerate(sura):

            candidate_PN       += count_arabic_letters(aya)
            test_len_memorised += candidate_PN

            if sura_name not in partition_suras:
                partition_suras.append(sura_name)

            if candidate_PN >= len_parition:
                print(f'Hizb Number ({partition_count} : {NUMBER_PARTITIONS})'); partition_count += 1
                print(f'Number of letters: {candidate_PN}')
                len_TEST += candidate_PN
                aya_number = i + 1
                print_suras_if_they_are_less_than_9(partition_suras)
                print(f'From: {hizb_begins_at}')
                print(f'Until: {sura_name} - {aya_number}')
                print(aya)
                print('-'*44)
                hizb_begins_at = f'{sura_name} - {aya_number+1}'
                candidate_PN = 0
                partition_suras = []

    print(f'Hizb Number ({partition_count} : {NUMBER_PARTITIONS})')
    print(f'Number of letters: {candidate_PN}')
    print(f'From: {hizb_begins_at}')
    print(f'Until: آخر القرءان')

    assert (len_TEST + candidate_PN) == len_memorized_quran, 'Partitions size does not sum up to memorized size'

if __name__ == '__main__':
    print_hizb(SuraNames.memorized, NUMBER_PARTITIONS=7)
