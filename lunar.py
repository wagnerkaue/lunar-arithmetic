class Lunar:
    def __init__(self, value):
        self.value = str(value)
        if any(digit != "0" for digit in self.value):
            self.value = self.value.lstrip("0")

    def __str__(self):
        return self.value

    def __add__(self, other):
        fill = len(max(self.value, other.value, key=len))
        zipped = zip(self.value.zfill(fill), other.value.zfill(fill))
        result = ""
        for self_d, other_d in reversed(list(zipped)):
            result += max(self_d, other_d)
        return Lunar(result[::-1])

    def __mul__(self, other):
        fill = len(max(self.value, other.value, key=len))
        list_to_add = []
        right_zeros = 0
        for multiplier in reversed(other.value.zfill(fill)):
            to_add = ""
            for multiplicand in reversed(self.value.zfill(fill)):
                to_add += min(multiplier, multiplicand)
            list_to_add.append(Lunar(to_add[::-1] + "0" * right_zeros))
            right_zeros += 1
        result = Lunar(0)
        for lun in list_to_add:
            result += lun
        return result

    def __pow__(self, other):
        # The multiplication neutral element in Lunar arithmetic is the larger digit of the number
        result = Lunar(max(int(digit) for digit in self.value))
        for _ in range(int(other.value)):
            result *= self
        return result
