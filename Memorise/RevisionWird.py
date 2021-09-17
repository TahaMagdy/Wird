import sys
sys.path.append('/Users/taha/cs')
import pyquran as q


class RevisionWird:
    def __init__(self
            , parts_count=6
            , memorized_suras_names_file='Hifz_taha.txt'):
        self.wird                 = dict()  # for example {'1:6' : '9999 البقرة'}
        self.parts_count          = parts_count
        self.memorized_suras_list = open(memorized_suras_names_file).readlines()


    def compute_wird(self):
        print('wird')



if __name__ == '__main__':
    wird = RevisionWird()
    wird.compute_wird()