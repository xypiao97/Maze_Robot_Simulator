from typing import List

class Representation_Map:
    @classmethod
    def show(cls, near_map: List):
        print("-" * 20)
        for col in near_map:
            print(col)
        print("-" * 20)