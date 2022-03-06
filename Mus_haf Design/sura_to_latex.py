import sys
sys.path.append('../..')

import pyquran as q
import os

suras_names_in_progress = open('../Memorise/suras_names_in_progress.txt', 'r').readlines()
print(suras_names_in_progress)
sura_name = 'المائدة'

def generate_sura_latex(sura_name):

    sura_name = sura_name.strip()

    sura_number = q.quran.get_sura_number(sura_name)
    sura = q.quran.get_sura(sura_number, with_tashkeel=True, basmalah=False)


    latex_file_name = f'{sura_number}-{sura_name}.tex'
    f = open(latex_file_name, 'w')
    top = open('top.tmp', 'r').read()


    f.write(top)
    out = []
    for number, text in enumerate(sura):
        number += 1
        latex_number = f'{{\\tiny\colorbox{{cl_aya}}{{{number}}}}}'
        line = latex_number + ' ' + text + '\n'
        f.write(line)


    f.write('\\end{document}')

    f.close()

    #subprocess.Popen('xelatex ')
    print(f'xelatex {latex_file_name}' )
    os.system(f'xelatex {latex_file_name}' )






if __name__ == '__main__':
    for sura_name in suras_names_in_progress:
        generate_sura_latex(sura_name)
