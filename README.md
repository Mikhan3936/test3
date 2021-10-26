.. test3 documentation master file, created by
   sphinx-quickstart on Tue Oct 26 03:51:09 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Документация по классам тестового задания №3
============================================

Список классов, используемых в модуле
-------------------------------------

- ## Общий класс
   ```python 

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
            
            pass
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
    ```
    - ## Образованный от него класс для расчета квадратов
    ```python 
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
   ```
    - ## Образованный от него класс для расчета прямоугольников
     ```python

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
    ```
    #.
    #.
    #.
    #.
    #.
    #.
    #.
    #.
    #.


