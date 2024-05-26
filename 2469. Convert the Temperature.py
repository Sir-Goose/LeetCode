class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = 0
        farenheit = 0

        kelvin = celsius + 273.15
        farenheit = celsius * 1.80 + 32

        return [kelvin, farenheit]
        
