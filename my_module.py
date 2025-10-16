## ++++++++++++++++++++++++++++++++++++++++++++++
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


## ++++++++++++++++++++++++++++++++++++++++++++++++++++++
class EvenOdd:
    def __init__(self, number):
        self.number = number

    def even(self):
        if self.number % 2 == 0:
            return True
        return False

    def odd(self):
        if self.number % 2 != 0:
            return True
        return False


## +++++++++++++++++++++++++++++++++++++++++++
class PrimeComposite:
    def __init__(self, number):
        self.number = number

    def prime(self):
        if self.number <= 1:
            return  False
        else:
            is_prime = True
            for m in range(2, self.number):
                if self.number % m == 0:
                    is_prime = False

            return is_prime
    
    def Composite(self):
        if self.number <= 1:
            return False
        
        else:
            for m in range(2, self.number):
                if self.number % m == 0:
                    return True   
            return False

