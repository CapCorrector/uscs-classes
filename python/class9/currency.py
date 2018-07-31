class CurrencyUnit:
    conversion = 1.0
    def __get__(self, instance, owner):
        return instance.usd * self.conversion
    def __set__(self, instance, value):
        instance.usd = value / self.conversion

class USD(CurrencyUnit):
    def __get__(self, instance, owner):
        return instance._usd
    def __set__(self, instance, value):
        instance._usd = value
        
class Euro(CurrencyUnit):
    conversion = 0.85

class Pound(CurrencyUnit):
    conversion = 0.75

class Rupee(CurrencyUnit):
    conversion = 67.53

class Currency:
    usd = USD()
    euro = Euro()
    pound = Pound()
    rupee = Rupee()

    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        if usd:
            self.usd = usd
        elif euro:
            self.euro = euro
        elif pound:
            self.pound = pound
        elif rupee:
            self.rupee = rupee
        else:
            raise TypeError

    def __str__(self):
        return '{:.2f} usd == {:.2f} euro == {:.2f} pound == {:.2f} rupee'.format(self.usd, self.euro, self.pound, self.rupee)

if __name__ == '__main__':
    currency = Currency(usd = 100)
    print(currency)
    currency.euro = 1000
    print(currency)
