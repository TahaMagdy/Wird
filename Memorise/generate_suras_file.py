import sys
sys.path.append('..')

import pyquran as q

f = open('suras_names_all_quran.txt', 'w')
for i in range(1, 114+1):
    name = q.quran.get_sura_name(i)
    f.write(name + '\n')

f.close()
