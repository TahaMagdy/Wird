import sys
sys.path.append('/Users/taha/cs')
import pyquran as q

# sura is (name, length)
class Sura:
    def __init__(self, name) -> None:
        self.name      = name
        self.text      = self.__get_sura(name)
        self.length    = len(self.text)

    def __repr__(self) -> str:
        out = f'[Sura] {self.length} {self.name}'
        return out

    def __get_sura(self, name):
        list_sura = q.quran.get_sura(q.quran.get_sura_number(name.strip()), basmalah=False)
        text_sura = ''.join(list_sura).strip()
        text_sura = text_sura.replace(' ', '')
        return text_sura


if __name__ == '__main__':
    x = Sura(name='الإخلاص')
    print(x)