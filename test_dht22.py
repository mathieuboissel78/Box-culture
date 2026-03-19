import board
import adafruit_dht

dht = adafruit_dht.DHT22(board.D4)

try:
    temperature = dht.temperature
    humidite = dht.humidity
    print(f'Température : {temperature:.1f}°C')
    print(f'Hygrométrie : {humidite:.1f}%')
except RuntimeError as e:
    print(f'Erreur de lecture : {e}')
finally:
    dht.exit()