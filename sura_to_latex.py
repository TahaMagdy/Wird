import sys
sys.path.append('..')

import pyquran as q

sura = q.quran.get_sura(q.quran.get_sura_number('النساء'), with_tashkeel=True, basmalah=False)

f = open('out.tex', 'w')
out = []
for number, text in enumerate(sura):
    number += 1
    latex_number = f'{{\\tiny\colorbox{{cl_aya}}{{{number}}}}}'
    line = latex_number + ' ' + text + '\n'
    f.write(line)


f.close()
