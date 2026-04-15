import schedule
import threading
import time
import config
from dashboard.app import app
import simulation
from sauvegarde import charger
from routines.climat import routine_climat
from routines.arrosage import routine_arrosage
from routines.surveillance import routine_surveillance
from routines.led import routine_led
from historique import initialiser_historique_db
from config_db import initialiser_config_db

initialiser_historique_db()
initialiser_config_db()
charger()
routine_surveillance()
routine_led()
routine_climat()

if config.SIMULATION:
	schedule.every(config.INTERVALLE_SECHAGE).seconds.do(simulation.assecher)
	schedule.every(config.INTERVALLE_TEMPERATURE).seconds.do(simulation.evoluer_temperature)
	schedule.every(2).minutes.do(simulation.alterner_led)

schedule.every(config.INTERVALLE_SURVEILLANCE).seconds.do(routine_surveillance)
schedule.every(10).minutes.do(routine_climat)
schedule.every(config.INTERVALLE_ARROSAGE).seconds.do(routine_arrosage)
schedule.every(1).minutes.do(routine_led)

def lancer_schedule():
	while True:
		schedule.run_pending()
		time.sleep(1)

thread = threading.Thread(target=lancer_schedule)
thread.daemon = True
thread.start()

app.run(host='0.0.0.0', port=5000)
