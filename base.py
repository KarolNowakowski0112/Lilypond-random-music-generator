import numpy as np


def init_file(path):
    f = open(path, "w")

    f.write('\\version "2.18.2"\n')
    f.write('\n')
    f.write('\\paper {\n')
    f.write('\t#(set-paper-size "a4")\n')
    f.write('}\n')
    f.write('\n')
    f.write('\\layout {\n')
    f.write('\tindent = 0\\in\n')
    f.write('\tragged-last = ##f\n')
    f.write('\t\\context {\n')
    f.write('\t\t\\Score\n')
    #f.write('\t\t\\remove "Bar_number_engraver"\n')
    f.write('\t}\n')
    f.write('}\n\n')

    return f


def set_scale(f, key, metrum):
    f.write('\\absolute {\n')
    height, key = key.split(' ')
    f.write('\t\\key ' + height + ' \\' + key +'\n')
    f.write('\t\\time ' + str(metrum) + '/4\n\n')
    f.write('\t\\override Score.BarNumber.break-visibility = ##(#t #t #t)\n')
    f.write('\t\\set Score.currentBarNumber = #1\n')
    f.write('\t\\bar ""\n\n')


def end_section(f):
    f.write('\n\t\\bar "||"')
    f.write('\n}\n')


def put_note(f, height, rythmicValue, dot, arc):
    if arc == 'jest':
        f.write('(')

    if dot == 1:
        f.write('\t' + height + str(rythmicValue) + '.')
    else:
        f.write('\t' + height + str(rythmicValue))

    if arc == 'jest':
        f.write(')')


def put_pause(f, rythmicValue):
    f.write('\t' + 'r' + str(rythmicValue))


def translate(n, *argv):
    # 0 - C0
    # 1 - D0
    # ...
    # 7 - C1
    # ...
    # 21 - c'
    # ...

    note = ''

    if n % 7 == 0:
        note += 'c'
    elif n % 7 == 1:
        note += 'd'
    elif n % 7 == 2:
        note += 'e'
    elif n % 7 == 3:
        note += 'f'
    elif n % 7 == 4:
        note += 'g'
    elif n % 7 == 5:
        note += 'a'
    elif n % 7 == 6:
        note += 'b'

    if len(argv) > 0:
        for i in range(len(argv)):
            if argv[i] == "is" or argv[i] == 'es' or argv[i] == 'isis' or argv[i] == 'eses':
                note += argv[i]

    if int(n / 7) == 0:
        note += ',,'
    elif int(n / 7) == 1:
        note += ','
    elif int(n / 7) == 2:
        note += ''
    elif int(n / 7) == 3:
        note += "'"
    elif int(n / 7) == 4:
        note += "''"
    elif int(n / 7) == 5:
        note += "'''"
    elif int(n / 7) == 6:
        note += "''''"

    return note


def reverse_translate(note):
    # C0 - 0
    # D0 - 1
    # ...
    # C1 - 7
    # ...
    # c' - 21
    # ...

    height = note[0]
    number = 14

    if len(note) > 1:
        char = note[1]
        if char == ",":
            number -= (len(note)-1)*7
        elif char == "'":
            number += (len(note)-1)*7

    if height == 'c':
        number += 0
    elif height == 'd':
        number += 1
    elif height == 'e':
        number += 2
    elif height == 'f':
        number += 3
    elif height == 'g':
        number += 4
    elif height == 'a':
        number += 5
    elif height == 'b':
        number += 6

    return number
