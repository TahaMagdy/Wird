import sys
sys.path.append('/Users/taha/cs')
import pyquran as q


class RevisionWird:
    def __init__(self, parts_count=6) -> None:
        self.parts_count          = parts_count
        self.memorized_suras_list = open('Hifz_taha.txt').readlines()
        self.wird = dict()  # for example {'1:6' : '9999 البقرة'}

    def compute_wird(self):
        print('wird')



if __name__ == '__main__':
    wird = RevisionWird()
    wird.compute_wird()