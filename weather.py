weather_data = {
    'Ташкент': '☀️ +26°C, солнечно',
    'Москва': '🌧 +14°C, дождь',
    'Дубай': '☀️ +35°C, жарко',
    'Лондон': '🌫 +12°C, туман'
}
message = input('Введите название города:')
if message in weather_data.keys():
    print('Погода в городе '+message+':'+weather_data[message])
elif message not in weather_data.keys():
    print('Нет данных о погоде для города '+message)



