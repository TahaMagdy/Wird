import MemoDict


get_memorized_or_not_memorized = \
    lambda predicate, your_quran: [ (name, number_of_ayat) for name, number_of_ayat in your_quran.items()
                                    if predicate(number_of_ayat) ]


def get_memorized(how_much_quran_do_you_know):
    memorized     = get_memorized_or_not_memorized(lambda n: n > 0, how_much_quran_do_you_know)
    return memorized


# TESTING

memorized     = get_memorized_or_not_memorized(lambda n: n > 0, MemoDict.quran)
not_memorized = get_memorized_or_not_memorized(lambda n: n == 0, MemoDict.quran)

assert len(memorized) + len(not_memorized) == 114 \
            , 'memorized + not_memorized != 114'
