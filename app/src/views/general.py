from flask import request, Blueprint, current_app, Response, render_template, session
from src import app
from redis import Redis
import json



general = Blueprint('general', __name__)
redis = Redis(host= "redis", port=6379)

healthy = True 
services_health = {
	"redis": False
}

@general.route("/health")
def check_status():
	global healthy
	global services_health
	health_check_pass = True
	try:
		redis.ping()
		services_health["redis"] = True
	except Exception as e:
		health_check_pass = False
		services_health["redis"] = False
		print(e)

	# we set healthy to the value of health_check_pass here
	# as it will reset the overall health status if a service was down in a previous check but is now avalible
	healthy = health_check_pass


	output = {
		"app": current_app.config["APP_NAME"],
		"healthy": healthy,
		"services_health": services_health,
		"host": current_app.config["HOSTNAME"]
	}

	if healthy:
		return Response(json.dumps(output), status=200, mimetype='application/json')
	else:
		return Response(json.dumps(output), status=500, mimetype='application/json')


@general.route("/")
def index():
	check_status()

	if not healthy:
		return "sorry something is currently wrong with this app, please try again later"
		
	if session.get("user_id"):
		user_id = session['user_id']
	else:
		user_id = redis.incr('hits')
		session['user_id'] = user_id

	return "your user id is {}".format(user_id)
