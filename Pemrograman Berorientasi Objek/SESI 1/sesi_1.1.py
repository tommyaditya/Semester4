class car:
    def __init__(self, brand, models,year):
        self.brand = brand
        self.models = models
        self.year = year


    def display_info(self):
        print(f'brand: {self.brand}, models: {self.models}, year: {self.year}')


car1 = car('honda', 'torbil', '1922')
car2 = car('inova', 'kijang', '3023')
car3 = car('toyota', 'civic', '2020')
car3.display_info()