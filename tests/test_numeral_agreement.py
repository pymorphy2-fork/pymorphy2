import pytest


@pytest.mark.parametrize(('word', 'result'), [
    # прилагательные
    ("бесплатная", ["бесплатная", "бесплатные", "бесплатных"]),
    ("бесплатный", ["бесплатный", "бесплатных", "бесплатных"]),

    # числительные
    ("первый", ["первый", "первых", "первых"]),
    ("первая", ["первая", "первые", "первых"]),

    # существительные
    ("книга", ["книга", "книги", "книг"]),
    ("болт", ["болт", "болта", "болтов"]),

    # причастия
    ("летящий", ["летящий", "летящих", "летящих"]),
    ("летящая", ["летящая", "летящие", "летящих"]),

    # остальное части речи мы никак не согласовываем с числами
    ("играет", ["играет", "играет", "играет"])
])
def test_plural_forms(word, result, morph):
    parsed = morph.parse(word)
    assert len(parsed)
    for plural, num in zip(result, [1, 2, 5]):
        assert parsed[0].make_agree_with_number(num).word == plural


@pytest.mark.parametrize(('word', 'form', 'result'), [
    ("книга", 'gent', ["книги", "книг", "книг"]),
    ("книга", 'datv', ["книге", "книгам", "книгам"]),
    ("книга", 'accs', ["книгу", "книги", "книг"]),
    ("книга", 'ablt', ["книгой", "книгами", "книгами"]),
    ("книга", 'loct', ["книге", "книгах", "книгах"]),

    ("час", "accs", ["час", "часа", "часов"]), # see https://github.com/kmike/pymorphy2/issues/32
    ("день", "accs", ["день", "дня", "дней"]),
    ("минута", "accs", ["минуту", "минуты", "минут"]),

    ("бесплатный", "gent", ["бесплатного", "бесплатных", "бесплатных"]),
    ("бесплатный", "datv", ["бесплатному", "бесплатным", "бесплатным"]),
    ("бесплатный", "accs,anim", ["бесплатного", "бесплатных", "бесплатных"]), # animacy make sense in accs
    ("бесплатный", "accs,inan", ["бесплатный", "бесплатных", "бесплатных"]),
    ("бесплатный", "ablt", ["бесплатным", "бесплатными", "бесплатными"]),
    ("бесплатный", "loct", ["бесплатном", "бесплатных", "бесплатных"]),

    ("бесплатная", "gent", ["бесплатной", "бесплатных", "бесплатных"]),
    ("бесплатная", "datv", ["бесплатной", "бесплатным", "бесплатным"]),
    ("бесплатная", "accs,anim", ["бесплатную", "бесплатных", "бесплатных"]),
    ("бесплатная", "accs,inan", ["бесплатную", "бесплатные", "бесплатных"]),
    ("бесплатная", "ablt", ["бесплатной", "бесплатными", "бесплатными"]),
    ("бесплатная", "loct", ["бесплатной", "бесплатных", "бесплатных"]),

    ("летящий", "gent", ["летящего", "летящих", "летящих"]),
    ("летящий", "datv", ["летящему", "летящим", "летящим"]),
    ("летящий", "accs,anim", ["летящего", "летящих", "летящих"]),
    ("летящий", "accs,inan", ["летящий", "летящих", "летящих"]),
    ("летящий", "ablt", ["летящим", "летящими", "летящими"]),
    ("летящий", "loct", ["летящем", "летящих", "летящих"]),

    ("летящая", "gent", ["летящей", "летящих", "летящих"]),
    ("летящая", "datv", ["летящей", "летящим", "летящим"]),
    ("летящая", "accs,anim", ["летящую", "летящих", "летящих"]),
    ("летящая", "accs,inan", ["летящую", "летящие", "летящих"]),
    ("летящая", "ablt", ["летящей", "летящими", "летящими"]),
    ("летящая", "loct", ["летящей", "летящих", "летящих"]),

    ("белка", "accs", ["белку", "белок", "белок"]),
    ("бобер", "accs", ["бобра", "бобров", "бобров"]),
    ("камень", "accs", ["камень", "камня", "камней"]),
    ("лопата", "accs", ["лопату", "лопаты", "лопат"])
])
def test_plural_inflected(word, form, result, morph):
    parsed = [p for p in morph.parse(word) if p.tag.case == 'nomn']
    assert len(parsed)
    gram_tag = morph.TagClass(form)
    inflected_word = parsed[0].inflect({gram_tag.case})
    if gram_tag.animacy and inflected_word.tag.animacy:
        # morph.parse('летящая')[0].inflect({'accs','inan'}).word == 'летящий'
        inflected_word = inflected_word.inflect({gram_tag.animacy})
    assert inflected_word.word == result[0]
    for plural, num in zip(result, [1, 2, 5]):
        assert inflected_word.make_agree_with_number(num, gram_tag.animacy).word == plural


@pytest.mark.parametrize(('word', 'num', 'result'), [
    ("лопата", 0, "лопат"),
    ("лопата", 1, "лопата"),
    ("лопата", 2, "лопаты"),
    ("лопата", 4, "лопаты"),
    ("лопата", 5, "лопат"),
    ("лопата", 6, "лопат"),
    ("лопата", 11, "лопат"),
    ("лопата", 12, "лопат"),
    ("лопата", 15, "лопат"),
    ("лопата", 21, "лопата"),
    ("лопата", 24, "лопаты"),
    ("лопата", 25, "лопат"),
    ("лопата", 101, "лопата"),
    ("лопата", 103, "лопаты"),
    ("лопата", 105, "лопат"),
    ("лопата", 111, "лопат"),
    ("лопата", 112, "лопат"),
    ("лопата", 151, "лопата"),
    ("лопата", 122, "лопаты"),
    ("лопата", 5624, "лопаты"),
    ("лопата", 5431, "лопата"),
    ("лопата", 7613, "лопат"),
    ("лопата", 2111, "лопат"),
])
def test_plural_num(word, num, result, morph):
    parsed = morph.parse(word)
    assert len(parsed)
    assert parsed[0].make_agree_with_number(num).word == result
