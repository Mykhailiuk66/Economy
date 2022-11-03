from flask import render_template, request
from app import app


@app.route('/', methods=['GET', 'POST'])
def functional_points():
    basic_dict = {
        'organic': [2.4, 1.05],
        'semi_distributed': [3.0, 1.12],
        'built_in': [3.6, 1.20],
        None: '',
    }

    dict_wigthts = {
        'EI': [3, 4, 6],
        'EO': [4, 5, 7],
        'EQ': [3, 4, 6],
        'ILF': [7, 10, 15],
        'EIF': [5, 7, 10],
    }

    dict_inputs = {
        'EI': ['EI', 'EI', 'EI'],
        'EO': ['EO', 'EO', 'EO'],
        'EQ': ['EQ', 'EQ', 'EQ'],
        'ILF': ['ILF', 'ILF', 'ILF'],
        'EIF': ['EIF', 'EIF', 'EIF'],
    }

    dict_name = {
        'EI': 'Зовнішні вводи',
        'EO': 'Зовнішні виводи',
        'EQ': 'Зовнішні запити',
        'ILF': 'Локальні внутрішні логічні файли',
        'EIF': 'Зовнішні інтерфейсні файли',
    }

    dict_factor_environment = {
        '1': [0, 1, 2, 3, 4, 5],
        '2': [0, 1, 2, 3, 4, 5],
        '3': [0, 1, 2, 3, 4, 5],
        '4': [0, 1, 2, 3, 4, 5],
        '5': [0, 1, 2, 3, 4, 5],
        '6': [0, 1, 2, 3, 4, 5],
        '7': [0, 1, 2, 3, 4, 5],
        '8': [0, 1, 2, 3, 4, 5],
        '9': [0, 1, 2, 3, 4, 5],
        '10': [0, 1, 2, 3, 4, 5],
        '11': [0, 1, 2, 3, 4, 5],
        '12': [0, 1, 2, 3, 4, 5],
        '13': [0, 1, 2, 3, 4, 5],
        '14': [0, 1, 2, 3, 4, 5],
    }

    dict_name_factor_environment = {
        '1': 'Обмін даними',
        '2': 'Розподілені функції ',
        '3': 'Продуктивніcть',
        '4': 'Інтенсивно використовувана конфігурація ',
        '5': 'Інтенсивність транзакцій',
        '6': 'Діалоговий ввід даних',
        '7': 'Ефективність для кінцевого користувача',
        '8': 'Оперативне обновлення',
        '9': 'Складність обробки даних',
        '10': 'Повторне використання',
        '11': 'Легкість установлення',
        '12': 'Простотавикористання',
        '13': 'Поширюваність',
        '14': 'Легкіcть зміни ',
    }

    dict_language_ratio = {
        'DOS': ['Пакетні файли DOS', 128],
        'Basic': ['Basic', 107],
        'PL_1': ['PL/1', 80],
        'C#': ['C#', 58],
        'LISP': ['Розширений LISP', 56],
        'Java': ['Java', 55],
        'JavaScript': ['JavaScript', 54],
        'C++': ['C++', 53],
        'visual_basic': ['Visual Basic', 50],
        'bd_lang': ['Мови баз даних', 40],
        'Acces': ['Acces', 38],
        'VBScript': ['VBScript', 38],
        'lang_support_accept': ['Мови підтримки прийняття', 35],
        'FoxPro_2_5': ['FoxPro 2.5', 34],
        'DELPHI': ['DELPHI', 29],
        'standart_oop': ['Стандартні обєктно орієнтовані', 29],
        'vb_net': ['VB.Net', 28],
        'standart_lang_4th': ['Стандартні 4-го покоління', 20],
        'html': ['HTML 3.0', 15],
        'sql': ['SQL', 13],
        'sql_forms': ['SQL Forms', 11],
        'Excel': ['Excel', 6],
    }

    sum_patams = 0
    for key in dict_wigthts:
        num = request.form.getlist(key)
        for inex, v in enumerate(num):
            try:
                sum_patams += int(v) * dict_wigthts[key][inex]
            except:
                sum_patams += 0

    sum_factors = 0
    for key in dict_name_factor_environment:
        try:
            factors = request.form.get(key)
            sum_factors += int(factors)
        except:
            sum_factors = 0

    VAF = 0.65 + (sum_factors * 0.01)
    AFP = sum_patams * VAF

    lang_coef = request.form.get('lang_coef')

    try:
        V = int(lang_coef) * AFP
    except:
        V = 0

    cocomo = request.form.get('basic')
    try:
        T = basic_dict[cocomo][0] * (V / 1000)**basic_dict[cocomo][1]
    except:
        T = 0




    return render_template('functional_points.html', T=T, V=V, dict_language_ratio=dict_language_ratio, AFP=AFP, 
                                                              VAF=VAF, num=sum_patams, dict_input=dict_inputs, 
                                                              name=dict_name, dict_factor_environment=dict_factor_environment, 
                                                              dict_name_factor_environment=dict_name_factor_environment)