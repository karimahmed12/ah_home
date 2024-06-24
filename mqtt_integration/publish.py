from paho.mqtt import client as mqtt_client
import ssl

# MQTT broker credentials
Broker = "a3aea2a70f7b43d1809561231ab50b37.s1.eu.hivemq.cloud"
port = 8883
client_id = "ESP8266Client1"
username = "ESP32"
password = "123456aA"

# Define the MQTT topics
Main_Room_Light_topic = "Main_Room"  # on/off
Personal_Room_topic = "Personal_Room"  # on/off
Garage_topic = "Garage"  # on/off
Outside_topic = "Outside"  # on/off
window_control_topic = "window_control"  # open/close
Garage_control_topic = "Garage_control"  # open/close
Door_control_topic = "Door_control"  # open/close
fan_control_topic = "fan_control"  # on/off
fan_speed_topic = "fan_speed"  # 0 - 5

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to the Broker")
        else:
            print(f"Failed to connect with code {rc}")

    client = mqtt_client.Client(client_id=client_id, protocol=mqtt_client.MQTTv311)
    client.username_pw_set(username, password)
    client.on_connect = on_connect

    # Disable certificate verification for testing (not recommended for production)
    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)

    client.connect(Broker, port)

    return client

def publish_message(topic, status):
    client = connect_mqtt()
    client.loop_start()  # Start the message loop in the background

    result = client.publish(topic, status)
    msg_status = result.rc
    if msg_status == mqtt_client.MQTT_ERR_SUCCESS:
        print(f"Message: {status} sent to topic {topic}")
    else:
        print(f"Failed to send message to topic {topic}")

    client.loop_stop()
    #client.disconnect()

if __name__ == '__main__':
    # This block is kept for manual testing, it won't be used when called via API
    status = input("Enter Main Room Light status (on/off): ")
    publish_message(Main_Room_Light_topic, status)

    status = input("Enter Personal Room status (on/off): ")
    publish_message(Personal_Room_topic, status)

    status = input("Enter Garage status (on/off): ")
    publish_message(Garage_topic, status)

    status = input("Enter Outside status (on/off): ")
    publish_message(Outside_topic, status)

    status = input("Enter Window Control status (open/close): ")
    publish_message(window_control_topic, status)

    status = input("Enter garage Control status (open/close): ")
    publish_message(Garage_control_topic, status)

    status = input("Enter Fan Control status (on/off): ")
    publish_message(fan_control_topic, status)

    status = input("Enter Fan Speed (0-5): ")
    publish_message(fan_speed_topic, status)
