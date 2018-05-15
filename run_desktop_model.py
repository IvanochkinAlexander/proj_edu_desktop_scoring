#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import pandas as pd
from gooey import Gooey, GooeyParser

@Gooey(language='russian', dump_build_config=True, program_name="Страховой скоринг")
# print ('hello')
def main():

    """Executing script"""

    desc = u'Введите параметр и нажмите "Запуск"'

    p = GooeyParser(description=desc)

    p.add_argument('-a', '--a', default=2, type=int, help='Кол-во перевозимых детей')
    p.add_argument('-b', '--b', default=25, type=int, help='Возраст водителя')
    p.add_argument('-c', '--c', default=3, type=int, help='Кол-во детей всего')
    p.add_argument('-d', '--d', default=2, type=int, help='Неизвестный параметр')
    p.add_argument('-e', '--e', default=4, type=int, help='Водительский стаж')
    p.add_argument('-f', '--f', default=2, type=int, help='Неизвестный параметр')
    p.add_argument('-s', '--s', default=3, type=int, help='Кол-во страховых случаев')
    p.add_argument('-i', '--i', default=2, type=int, help='Неизвестный параметр')
    p.add_argument('-k', '--k', default=1, type=int, help='Возраст автомобиля')
    p.add_argument('-m', '--m', default=2, type=int, help='Неизвестный параметр')

    global args
    args = p.parse_args()

    with open ('xgb_model.pickle', 'rb') as f:
        clf_2 = pickle.load(f)

    result = clf_2.predict_proba(pd.DataFrame([args.a, args.b, args.c, args.d, args.e, args.f, args.s, args.i, args.k, args.m]).T)[0][0]

    print 'вероятность наступления страхового случая составляет : {} процентов'.format(result)

if __name__ == '__main__':
    main()
