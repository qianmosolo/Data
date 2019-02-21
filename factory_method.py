class English:
    def get(self, msg):
        return str('eng-' + msg)


class Chinese:
    def get(self, msg):
        return str('han-' + msg)


def get_localizer(lang='English'):
    langs = dict(English=English, Chinese=Chinese)
    return langs[lang]()


if __name__ == '__main__':
    eng, chi = get_localizer(), get_localizer('Chinese')
    print(eng.get('1'), chi.get('2'))
