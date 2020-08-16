from random import choice


def make_laugh(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehehe'))
        return f"{laugh} {person}"
    return get_laugh


laugh_at = make_laugh('Mustafa')
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
