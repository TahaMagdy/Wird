""" How much should I revisie quran to finish my (memorized suras) in N days?
"""


import sys
sys.path.append('/Users/tahamagdy/MacBook-13/cs')
sys.path.append('/Users/tahamagdy/MacBook-13/cs/quran')
import pyquran as q
import math

import MemorizedQuran
import ComputeMemorization

def get_memorized_sura_text_dict(memorized_sura_aya):
    '''
    {
        'suraName': [aya_1, aya_2, ..., aya_n]
    }
    '''

    memorized_sura_text_dict = dict()

    for sura_name, length in memorized_sura_aya:
        sura_as_list = q.quran.get_sura(q.quran.get_sura_number(sura_name.strip()), basmalah=False)

        memorized_sura_text_dict[sura_name] = sura_as_list[:length]

    return memorized_sura_text_dict


def get_memorized_sura_as_one_string(suras_names: list, dict_memorized_sura_aya: dict):
    ayat_one_list = []
    for sura_name, _ in suras_names:
        sura_as_list = dict_memorized_sura_aya[sura_name]
        ayat_one_list += sura_as_list

    one_string = ' '.join(ayat_one_list)
    return one_string


def count_arabic_letters(aya):
    x = 0
    for char in aya:
        if char in q.arabic.alphabet:
            x += 1
    return x


def print_hizb(memorized_sura_names, NUMBER_PARTITIONS=7):


    memorized_text_dict = get_memorized_sura_text_dict(memorized_sura_names)
    memorized_string = get_memorized_sura_as_one_string(memorized_sura_names, memorized_text_dict)

    len_memorized_quran = count_arabic_letters(memorized_string)
    len_parition        = math.floor(len_memorized_quran / NUMBER_PARTITIONS)

    print('>> ', len_parition, len_memorized_quran, len_memorized_quran / len_parition)
    print()

    candidate_PN       = 0
    test_len_memorised = 0
    len_TEST           = 0
    partition_count    = 1
    partition_suras    = []

    for sura_name, _ in memorized_sura_names:
        sura = memorized_text_dict[sura_name]

        for i, aya in enumerate(sura):

            candidate_PN       += count_arabic_letters(aya)
            test_len_memorised += candidate_PN

            if sura_name not in partition_suras:
                partition_suras.append(sura_name)

            if candidate_PN >= len_parition:
                print(f'Hizb ({partition_count} : {NUMBER_PARTITIONS})'); partition_count += 1

                print(f'# letters: {candidate_PN:,}')
                len_TEST += candidate_PN
                aya_number = i + 1
                print('، '.join(partition_suras))

                first_7_tokens_aya = ' '.join(aya.split(' ')[:7])
                # print(f'حتى {sura_name} ({aya_number}) {first_7_tokens_aya}')
                print(f'({aya_number}) {first_7_tokens_aya}')
                
                print('-'*44)
                candidate_PN = 0
                partition_suras = []

    print(f'Hizb Number ({partition_count} : {NUMBER_PARTITIONS})')
    print(f'Number of letters: {candidate_PN:,}')
    print(f'حتى آخر القرءان')

    assert (len_TEST + candidate_PN) == len_memorized_quran, 'Partitions size does not sum up to memorized size'


def get_number_of_paritions():
    import sys
    if len(sys.argv) < 2:
        print('Please enter the number of partitions: as a command line arg')
        sys.exit()
    return int(sys.argv[1])



if __name__ == '__main__':

    n = get_number_of_paritions()
    memorized = ComputeMemorization.get_memorized(MemorizedQuran.quran_taha)
    print_hizb(memorized, NUMBER_PARTITIONS=n)



