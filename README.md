# MQTT


Add user
---------

	$ echo "<user>:<password>" > /etc/mosquitto/pwfile
	$ mosquitto_passwd -U /etc/mosquitto/pwfile``
	    
		  
Edit /etc/mosquitto/mosquitto.conf
----------------------------------

	Uncomment or Add : password_file /etc/mosquitto/pwfile
	Uncomment or Add : allow_anonymous false


Run mosquitto service
---------------------

	$ su service mosquitto start


Publisher
----------

	Send data to broker.


Subscriber
----------

	Receive data from broker.


