#!/usr/bin/env python3
class Dog:
    def __init__(self, name='Dog'):
        self.name = name

    def bark(self):
        print("Woof!")

    def sit(self):
        if self.name == 'Dog':
         print("The dog is sitting.")
        else:
           print(f"The dog {self.name} is sitting.")