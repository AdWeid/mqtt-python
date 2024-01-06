import time
import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "192.168.1.222"
broker_port = 1883

# MQTT topic to publish to
mqtt_topic = "CPT"  # Replace with the actual topic you want to use

# Initialize MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Variable to be published
cpt = 0

try:
    while cpt <= 60:
        # Publish the value of "cpt" to the MQTT topic
        client.publish(mqtt_topic, str(cpt))

        # Increment "cpt"
        cpt += 1
        print(cpt)

        # Wait for a moment (adjust as needed)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Disconnect from the MQTT broker
    client.disconnect()
