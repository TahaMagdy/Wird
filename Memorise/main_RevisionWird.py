import sys
sys.path.append('/Users/tahamagdy/MacBook-13/cs/')
import pyquran as q


def sum_groups_len(list_of_suras):
    out = 0
    for sura in list_of_suras:
        out += sura.length
    return out


def print_groups_sizes(partitions):
    for i, key_value in enumerate(partitions.items()):
        key, value = key_value
        print(key)
        print(value)
        print(f'{i+1}:{self.parts_count} ', sum_groups_len(value))


#################################################
from Sura import Sura
class RevisionWird:
    def __init__(self
            , parts_count=6
            , memorized_suras_names_file='suras_names_finished_taha.txt'):
        self.wird                       = dict()  # for example {'1:6' : [sura] }
        self.parts_count                = parts_count
        self.memorized_suras_names_list = open(memorized_suras_names_file).readlines()
        self.sorted_memorized_suras     = self.get_memorized_sorted_suras()
        self.compute_wird()


    def __repr__(self) -> str:
        out = ''
        dash = '-'
        hizb =  'الحزب'
        for partition_number, list_suras in self.wird.items():
            out += '\n\n'
            out += f'{hizb} {partition_number}\n'
            out += f'{dash*9}\n'
            for sura in list_suras:
                out += f'{sura.length} {sura.name}'
        out = out.strip()
        return out


    def get_memorized_sorted_suras(self):
        # * Preparing a sorted list of Sura
        tmp_sura_list = []
        for sura_name in self.memorized_suras_names_list:
            sura  = Sura(name=sura_name)
            tmp_sura_list.append(sura)

        # * Sorting tmp_sura_list: [(sura_name, sura_length)]
        tmp_sura_list.sort(key=lambda sura: sura.length, reverse=True)
        assert len(tmp_sura_list) == len(self.memorized_suras_names_list)

        return tmp_sura_list


    def get_minimum_part_key(self, parts):
        minimum_length = float('inf')
        key_minimum_len_part = ''

        for key, list_of_suras in parts.items():
            sum_group = sum_groups_len(list_of_suras)
            if minimum_length > sum_group:
                minimum_length = sum_group
                key_minimum_len_part = key

        return key_minimum_len_part


    def compute_wird(self):
        for i, sura in enumerate(self.sorted_memorized_suras):
            if len(self.wird.keys()) < self.parts_count:
                key = f'{i+1}:{self.parts_count}'
                self.wird[key] = [ sura ]
                continue
            key_minimum_len_part = self.get_minimum_part_key(self.wird)
            self.wird[key_minimum_len_part].append( sura )



if __name__ == '__main__':
    from functools import reduce
    wird = RevisionWird(parts_count=14)
    print(wird)
    for i, suras in wird.wird.items():
        print(suras[0].length)
        # m = sum(map(lambda sura: sura.length, suras))
        m = list(map(lambda sura: sura.length, suras))
        print(m)
        print(sum(m))