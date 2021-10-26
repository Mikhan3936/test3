#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:05:40 2021
Тестовое задание № 3 по теме ООП
@author: Поздняков Михаил
"""
# import unittest

class fig():
    count = 0
    def __init__(self, x = 0):
        self.count += 1
        self.pi = 3.14159
        self.__color = 'red'
        if isinstance(self, kvadrat):
            self.length = x
        elif isinstance(self, rectangle):
            self.length = x
            self.height = 0
        elif isinstance(self, triangle):
            self.length = x
            self.height = 0
        elif isinstance(self, trapezoid):
            self.length = x
            self.height = 0
        elif isinstance(self, rhombus):
            self.length = x
            self.height = 0
        elif isinstance(self, cube):
            self.length = x
        elif isinstance(self, circle):
            self.radius = x
        elif isinstance(self, sphere):
            self.radius = x
        elif isinstance(self, parallepiped):
            self.length = x
            self.height = 0
            self.width = 0
        elif isinstance(self, pyramid):
            # сложно - используем 4х стороннюю пирамиду
            self.length = x
            self.height = 0
        elif isinstance(self, cylinder):
            self.radius = x
            self.height = 0
        elif isinstance(self, cone):
            self.radius = x
            self.height = 0
    def __del__(self):
        self.count -= 1
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color = 'red'):
        self.__color = color
        

class kvadrat(fig):
    arg = 1
    def __init__(self, x):
        super().__init__(x)
        self.arg = 1
    @classmethod
    def info(cls):
        print("Сторона")
        
    def square(self) -> float:
        return self.length ** 2

  
class rectangle(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.height = y
        self.arg = 2
    @classmethod
    def info(cls):
        print("Сторона")
        print("Сторона2")
    def square(self) -> float:
        return self.length * self.height

class triangle(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.height = y
        self.arg = 2
    @classmethod
    def info(cls):
        print("Сторона")
        print("Высота")
    def square(self) -> float:
        return self.length * self.height / 2

class trapezoid(fig):
    arg = 3
    def __init__(self, x, y, z):
        super().__init__(x)
        self.height = y
        self.length2 = z
        self.arg = 3
    @classmethod
    def info(cls):
        print("Нижняя часть")
        print("Высота")
        print('Верхняя часть')
    def square(self) -> float:
        return (self.length + self.length2) / 2 * self.height

class rhombus(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.height = y
        self.arg = 2
    @classmethod
    def info(cls):
        print("Длина")
        print("Высота")
    def square(self) -> float:
        return self.length * self.height / 2


class cube(fig):
    arg = 1
    def __init__(self, x):
        super().__init__(x)
        self.arg = 1
    @classmethod
    def info(cls):
        print("Сторона")
    def square(self) -> float:
        return self.length ** 2 * 6


class circle(fig):
    arg = 1
    def __init__(self, x):
        super().__init__(x)
        self.radius = x
        self.arg = 1
    @classmethod
    def info(cls):
        print("Радиус")
    def square(self) -> float:
        return self.radius ** 2 *self.pi

class sphere(fig):
    arg = 1
    def __init__(self, x):
        super().__init__(x)
        self.radius = x
        self.arg = 1
    @classmethod
    def info(cls):
        print("Радиус")
    def square(self) -> float:
        return self.radius ** 2 * 4 * self.pi

class parallepiped(fig):
    arg = 3
    def __init__(self, x, y, z):
        super().__init__(x)
        self.height = y
        self.length2 = z
        self.arg = 3
    @classmethod
    def info(cls):
        print("Сторона")
        print("Высота")
        print('Сторона2')
    def square(self) -> float:
        bok = (self.length + self.length2) * 2 * self.height
        return self.length * self.length2 * 2 +bok

class pyramid(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.height = y
        #self.apothema = z
        self.arg = 2
    @classmethod
    def info(cls):
        print('Правильная четырехгранная пирамида')
        print("Сторона")
        print("Высота")
        #print('Апофема')
    def square(self) -> float:
        #osn = self.length ** 2
        #bok = self.apothema / 2 * (self.length * 4)
        return self.height * self.length / 2 * 4
    
class cylinder(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.radius = x
        self.height = y
        self.arg = 2
    @classmethod
    def info(cls):
        print("Радиус")
        print("Высота")
    def square(self) -> float:
        return self.radius * 2 * self.pi * (self.radius + self.height)
    
class cone(fig):
    arg = 2
    def __init__(self, x, y):
        super().__init__(x)
        self.radius = x
        self.height = y
        self.arg = 2
    @classmethod
    def info(cls):
        print("Радиус")
        print("Высота")
    def square(self) -> float:
        return self.radius ** 2 * self.pi * self.height /3
   




def main():
    # Словари обернуты в список для сохранения порядка следования
    st1 = [{'name': kvadrat, 'text': '0  - Треугольник'}, {'name': rectangle, \
         'text': '1  - Прямоугольник'}, {'name': triangle, 'text': '2  - Треугольник'},\
        {'name': trapezoid, 'text': '3  - Трапеция'}, {'name': rhombus, 'text': '4  - Ромб'},\
        {'name': cube, 'text': '5  - Куб'}, {'name': circle, 'text': '6  - Круг'}, {'name': sphere, 'text': '7  - Сфера'},\
        {'name': parallepiped, 'text': '8  - Параллепипед'}, {'name': pyramid, 'text': '9  - Пирамида'},\
        {'name': cylinder, 'text': '10 - Цилиндр'}, {'name': cone, 'text': '11 - Конус'}]
    st2 = ['0','1','2','3','4','5','6','7','8','9','10','11']
    # 1я менюшка
    
    for i in range(len(st1)):
        print(st1[i]['text'])
    print('Введите номер рассчитываемой фигуры')
    x = input()
    if x in st2:
        name1 = st1[int(x)]['name']
        print('Введите следующие параметры:')
        print(name1.info())
        z = []
        for i in range(name1.arg):
            while True:
                ss = input()
                if ss.isalpha():
                    print('Только цифры, введи еще раз!')
                    continue
                else:
                    z.append(int(ss))
                    break
        obj = st1[int(x)]['name'](*z)
        obj.color = 'blue'

    else:
        print('Введено некорректное значение считаем что это 0')
    print('Площадь фигуры=', obj.square())
    #print(s.height, s.length, s.color, name1)
    






if __name__ == '__main__':
    main()
