# MQTT


Add user
---------

	$ echo "<user>:<password>" > /etc/mosquitto/pwfile
	$ mosquitto_passwd -U /etc/mosquitto/pwfile
	    
		  
Edit /etc/mosquitto/mosquitto.conf
----------------------------------

	Uncomment or Add : password_file /etc/mosquitto/pwfile
	Uncomment or Add : allow_anonymous false


Run mosquitto service
---------------------

	$ su service mosquitto start


OR


Pull Docker image
-----------------
	$ docker pull aghadge/mosquitto
	$ docker run -it docker.io/aghadge/mosquitto


Publisher
----------

	Send data to broker.
	$ python publisher.py


Subscriber
----------

	Receive data from broker.
	# python subscriber.py


