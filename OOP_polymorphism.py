class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def displayNum(self):
        print(self.real, "i", "+", self.img, "j")

    def __add__(self, num2):
        self.newReal = self.real + num2.real
        self.newImg = self.img + num2.img
        return Complex(self.newReal, self.newImg)
    
    def __sub__(self, num2):
        self.newReal = self.real - num2.real
        self.newImg = self.img - num2.img
        return Complex(self.newReal, self.newImg)
    
num1 = Complex(2, 7)       
num1.displayNum()
num2 = Complex(8, 9)       
num2.displayNum()
print("_"*10)
# num3 = num1.add(num2)
num3 = num1- num2
num3.displayNum()