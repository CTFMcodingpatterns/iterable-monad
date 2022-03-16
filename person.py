from distutils.command.build_scripts import first_line_re


class Person:
    def __init__(self, first, last, city):
        self.first = first
        self.last = last
        self.city = city
