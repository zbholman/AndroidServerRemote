class TemperatureError(Exception):
    pass


class Temperature(object):
    def __init__(self, temp=None, scale='C'):
        self._celcius = None
        self._fahrenheit = None
        if temp:
            if scale in ('c', 'C'):
                self.celcius = temp
            elif scale in ('f', 'F'):
                self.fahrenheit = temp
            else:
                raise TemperatureError

    @property
    def celcius(self):
        return self._celcius

    @celcius.setter
    def celcius(self, temp):
        self._celcius = float('{0:.2f}'.format(temp))
        self._fahrenheit = float('{0:.2f}'.format((temp - 32) * 5 / 9))

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, temp):
        self._celcius = float('{0:.2f}'.format(temp * 9 / 5 + 32))
        self._fahrenheit = float('{0:.2f}'.format(temp))
