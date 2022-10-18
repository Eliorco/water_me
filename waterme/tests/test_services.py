# import unittest
# from services.weather import get_weather_by_url

# class TestServices(unittest.TestSuite):

#     def test_weather_sanity(self):
#         # Arrange
#         WEATHER_API_KEY = 'asdfghjklkjhgfdsxcvf4rfv6yh8iu'
#         lat,lon= 32.11067549435341, 34.82060004079175
#         url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric'
#         # Act
#         result = get_weather_by_url(url)
#         # Assert
#         self.assertEqual(result['cod'], 200)

# if __name__ == '__main__':
#     unittest.main()