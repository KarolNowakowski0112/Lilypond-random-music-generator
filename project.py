from base import init_file, set_scale, end_section, put_note, put_pause, translate, reverse_translate
import numpy as np
import random


def load_config(path):
    try:
        file = open(path, 'r')
        lines = file.readlines()
        file.close()

        cfg = {}
        for line in lines:
            key, value = line.replace('\n', '').split('=')
            cfg[key] = value

        cfg['metrum'] = int(cfg['metrum'])
        cfg['takty'] = int(cfg['takty'])
        cfg['p_pauzy'] = float(cfg['p_pauzy'])
        cfg['p_kropki'] = float(cfg['p_kropki'])
        cfg['p_1'] = float(cfg['p_1'])
        cfg['p_2m'] = float(cfg['p_2m'])
        cfg['p_2w'] = float(cfg['p_2w'])
        cfg['p_3m'] = float(cfg['p_3m'])
        cfg['p_3w'] = float(cfg['p_3w'])
        cfg['p_4'] = float(cfg['p_4'])
        cfg['p_4zw'] = float(cfg['p_4zw'])
        cfg['p_5'] = float(cfg['p_5'])
        cfg['p_6m'] = float(cfg['p_6m'])
        cfg['p_6w'] = float(cfg['p_6w'])
        cfg['p_7m'] = float(cfg['p_7m'])
        cfg['p_7w'] = float(cfg['p_7w'])
        cfg['p_8'] = float(cfg['p_8'])

    except Exception as e:
        print('Error:', e, '// using default config')
        cfg = {
            'metrum': 4,
            'takty': 20,
            'dz_pocz': "c'",
            'dz_najnizszy': "a",
            'dz_najwyzszy': "b''",
            'p_pauzy': 0.1, 'p_kropki': 0.2,
            'p_1': 0.1, 'p_2m': 0.1, 'p_2w': 0.1, 'p_3m': 0.05, 'p_3w': 0.1, 'P_4': 0.1, 'p_4zw': 0.05,
            'p_5': 0.1, 'p_6m': 0.05, 'p_6w': 0.05, 'p_7m': 0.05, 'p_7w': 0.05, 'p_8': 0.1,
        }

    return cfg


config = load_config('config/config_file.cfg')


def rand_interval(cfg):

    intervals = ['p_1', 'p_2m', 'p_2w', 'p_3m', 'p_3w', 'p_4', 'p_4zw', 'p_5', 'p_6m', 'p_6w', 'p_7m', 'p_7w', 'p_8']
    probabilities = [cfg['p_1'], cfg['p_2m'], cfg['p_2w'], cfg['p_3m'], cfg['p_3w'], cfg['p_4'], cfg['p_4zw'],
                     cfg['p_5'], cfg['p_6m'], cfg['p_6w'], cfg['p_7m'], cfg['p_7w'], cfg['p_8']]

    interval = np.random.choice(intervals, 1, p=probabilities)
    interval = str(interval)
    interval = interval.split("'")
    interval = interval[1]
    interval = interval.split("_")
    interval = interval[1]

    # Po powyzszych operacjacj zmienne 'interval' posiada jedynie cyfre odpowiednia dla danego interwalu
    # i ewentualnie literke 'm', 'w', lub 'zw'

    grades = 0
    semitones = 0

    if interval == '1':
        grades = 0
        semitones = 0
    elif interval == '2m':
        grades = 1
        semitones = 1
    elif interval == '2w':
        grades = 1
        semitones = 2
    elif interval == '3m':
        grades = 2
        semitones = 3
    elif interval == '3w':
        grades = 2
        semitones = 4
    elif interval == '4':
        grades = 3
        semitones = 5
    elif interval == '4zw':
        grades = 3
        semitones = 6
    elif interval == '5':
        grades = 4
        semitones = 7
    elif interval == '6m':
        grades = 5
        semitones = 8
    elif interval == '6w':
        grades = 5
        semitones = 9
    elif interval == '7m':
        grades = 6
        semitones = 10
    elif interval == '7w':
        grades = 6
        semitones = 11
    elif interval == '8':
        grades = 7
        semitones = 12

    #up_or_down = np.random.randint(2)  # Losuje 0 lub 1
    up_or_down = 1

    return grades, semitones, up_or_down


def is_czy_es(stopnie, poltony, aktualna_wys, wysokosc, gora_dol, is_es):

    if gora_dol == 1:  # Idziemy w gore
        if aktualna_wys % 7 <= 2:
            if stopnie > 2:
                if wysokosc % 7 > 2:
                    # przechodzi prze e -> f
                    if stopnie * 2 == poltony + 1:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
                else:
                    # przechodzi przez e -> f i przez b -> c
                    if stopnie * 2 == poltony + 2:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'
            else:
                if wysokosc % 7 > 2:
                    # przechodzi przez e -> f
                    if stopnie * 2 == poltony:
                        add_is_es = 'is'
                    else:
                        add_is_es = ''
                else:
                    # nie przechodzi nigdzie
                    if stopnie * 2 == poltony:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
        else:     # akt_wys % 7 jest od 3 do 6
            if stopnie > 3:
                if wysokosc % 7 < 2:
                    # przechodzi przez b -> c
                    if stopnie * 2 == poltony + 1:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
                else:
                    # przechodzie przez b -> c i przez e -> f
                    if stopnie * 2 == poltony + 2:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'
            else:
                if wysokosc % 7 < 2:
                    # przechodzi przez b -> c
                    if stopnie * 2 == poltony:
                        add_is_es = 'is'
                    else:
                        add_is_es = ''
                else:
                    # nie przechodzi nigdzie
                    if stopnie * 2 == poltony:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
    else:   # Idziemy w dol
        if aktualna_wys % 7 >= 3:
            if stopnie > 3:
                if wysokosc % 7 < 3:
                    # przechodzi przez f -> e
                    if stopnie * 2 == poltony + 1:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'
                else:
                    # przechodzi przez f -> e i przez c -> b
                    if stopnie * 2 == poltony + 2:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
            else:
                if wysokosc % 7 < 3:
                    # przechodzi przez f -> e
                    if stopnie * 2 == poltony:
                        add_is_es = 'es'
                    else:
                        add_is_es = ''
                else:
                    # nie przechodzi nigdzie
                    if stopnie * 2 == poltony:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'
        else:      # akt_wys jest od 0 do 2
            if stopnie > 2:
                if wysokosc % 7 > 2:
                    # przechodzi przez c -> b
                    if stopnie * 2 == poltony + 1:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'
                else:
                    # przechodzi przez c -> b i przez f -> e
                    if stopnie * 2 == poltony + 2:
                        add_is_es = ''
                    else:
                        add_is_es = 'es'
            else:
                if wysokosc % 7 > 2:
                    # przechodzi przez c -> b
                    if stopnie * 2 == poltony:
                        add_is_es = 'es'
                    else:
                        add_is_es = ''
                else:
                    # nie przechodzi nigdzie
                    if stopnie * 2 == poltony:
                        add_is_es = ''
                    else:
                        add_is_es = 'is'

    if is_es == 'is':
        if add_is_es == 'is':
            is_es = 'isis'
        elif add_is_es == 'es':
            is_es = ''
        else:
            is_es = 'is'
    elif is_es == 'es':
        if add_is_es == 'es':
            is_es = 'eses'
        elif add_is_es == 'is':
            is_es = ''
        else:
            is_es = 'es'
    elif is_es == 'isis':
        if add_is_es == 'is':
            wysokosc += 1
            is_es = 'is'
        elif add_is_es == 'es':
            is_es = 'is'
        else:
            is_es = 'isis'
    elif is_es == 'eses':
        if add_is_es == 'es':
            wysokosc -= 1
            is_es = 'es'
        elif add_is_es == 'is':
            is_es = 'es'
        else:
            is_es = 'eses'
    else:
        is_es = add_is_es

    return wysokosc, is_es


def melody(cfg):
    f = init_file('scores/melody.ly')
    set_scale(f, 'c major', cfg['metrum'])

    takty = cfg['takty']
    p_pauzy = cfg['p_pauzy']
    p_kropki = cfg['p_kropki']
    wysokosc = reverse_translate(cfg['dz_pocz'])
    wys_dolna = reverse_translate(cfg['dz_najnizszy']) + 1
    wys_gorna = reverse_translate(cfg['dz_najwyzszy']) - 1
    is_es = ''
    kropka = 0
    luk = 'none'

    rytmy = [1, 2, 4, 8, 16]

    # Losowanie wartosci rytmicznej od szesnastki do calej nuty, lub mniejszej wartosci gdy nie pozwala na to metrum

    if cfg['metrum'] >= 4:
        rytm_pocz = rytmy[random.randint(0, 4)]
    elif 4 > cfg['metrum'] >= 2:
        rytm_pocz = rytmy[random.randint(1, 4)]
    else:
        rytm_pocz = rytmy[random.randint(2, 4)]

    put_note(f, cfg['dz_pocz'], rytm_pocz, kropka, luk)

    dostepny_rytm = cfg['metrum']/4 - 1/rytm_pocz
    ctr = 0

    while True:

        # Gdy dostepny rytm wynosi 0 to znaczy ze skonczyl sie takt, wiec zaczyna sie uzupelnianie kolejngo
        # chyba, ze byl to ostatni takt zgodnie ze zdefiniowana ich liczba w pliku .cfg - wtedy konczy sie petla

        if dostepny_rytm == 0:
            ctr += 1
            dostepny_rytm = cfg['metrum']/4

        if ctr == takty:
            break

        # W zaleznosci od dostepnego miejsca w takcie losowana jest taka wartosc, aby nie przekroczyc
        # tej zdefiniowanej jako metrum w jednym takcie

        if dostepny_rytm == 1/16:
            rytm = rytmy[4]
        elif 1/4 > dostepny_rytm >= 1/8:
            rytm = rytmy[random.randint(3, 4)]
        elif 1/2 > dostepny_rytm >= 1/4:
            rytm = rytmy[random.randint(2, 4)]
        elif 1 > dostepny_rytm >= 1/2:
            rytm = rytmy[random.randint(1, 4)]
        else:
            rytm = rytmy[random.randint(0, 4)]

        if dostepny_rytm >= (1 / rytm) + (1 / (2 * rytm)) and (rytm == 2 or rytm == 4 or rytm == 8):
            kropka = np.random.choice(2, 1, p=[1 - p_kropki, p_kropki])
        else:
            kropka = 0

        # Losowanie interwalu za pomoca funckji zwracajacej liczbe stopni, liczbe poltonow
        # oraz informacje o tym czy idziemy w gore czy w dol 5-linii

        stopnie, poltony, gora_dol = rand_interval(cfg)

        aktualna_wysokosc = wysokosc
        pom_gora_dol = gora_dol

        # Obliczanie nowej wysokosci sprawdzajac czy nie wykracza ona poza zdefiniowany zakres

        if gora_dol == 0:   # w dol
            if wysokosc - stopnie > wys_dolna:
                wysokosc -= stopnie
            else:
                wysokosc += stopnie
                pom_gora_dol = 1
        elif gora_dol == 1:  # w gore
            if wysokosc + stopnie < wys_gorna:
                wysokosc += stopnie
            else:
                wysokosc -= stopnie
                pom_gora_dol = 0

        # Funckja zwraca nowa wysokosc, ktora moze sie zmienic w przypadku gdy do 'is' trzeba dodac kolejny
        # lub do 'es' trzeba dodac kolejny oraz informacje o tym, czy dla nowej wysokosci tez nalezy przypisac
        # 'is' lub 'es' albo '' gdy nic

        new_wysokosc, new_is_es = is_czy_es(stopnie, poltony, aktualna_wysokosc, wysokosc, pom_gora_dol, is_es)

        wysokosc = new_wysokosc
        is_es = new_is_es

        # Losowanie 0 (brak pauzy) lub 1 (pauza) z zadanym prawdopodobienstwem

        pauza = np.random.choice(2, 1, p=[1 - p_pauzy, p_pauzy])

        # Wprzypadku gdy nie zostala wylosowana pauza i sasiednie dzwieki znajduja sie na tej samej wysokosci
        # dodany zostaje luk

        if pauza == 0:
            if aktualna_wysokosc == wysokosc:
                if luk == 'jest':
                    luk = 'none'
                else:
                    luk = 'jest'
            else:
                if luk == 'jest':
                    luk = 'byl'
            nuta = translate(new_wysokosc, is_es)
            put_note(f, nuta, rytm, kropka, luk)
        else:
            put_pause(f, rytm)

        if kropka == 1 and pauza == 0:
            zajety_rytm = (1 / rytm) + (1 / (2 * rytm))
        else:
            zajety_rytm = 1 / rytm

        dostepny_rytm -= zajety_rytm

    end_section(f)


def main():
    melody(config)


if __name__ == "__main__":
    main()
