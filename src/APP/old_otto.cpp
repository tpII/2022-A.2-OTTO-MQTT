#include "Oscilador.h"
#include "Mqtt.h"

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "Otto";
const char* password = "OttoPassword";


WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

//--------------------------------------
// funcion para setear wifi llamada una sola vez
//--------------------------------------
void setup_wifi() {
  WiFi.begin(ssid, password);

  // while (WiFi.status() != WL_CONNECTED) {
  //   delay(500);
  //   Serial.print(".");
  // }
  // Serial.println("WiFi connected");
}

//--------------------------------------
// funcion callback llamada cada vez
// que llega un mensaje MQTT del broker
//--------------------------------------
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived on topic: '");
  Serial.print(topic);
  Serial.print("' with payload: ");
  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  mqttClient.publish(mqttTopicOut,("ESP8266: Cedalo Mosquitto is awesome. ESP8266-Time: "));
}

//--------------------------------------
// funcion connect llamada para reconectar
// a el broker
//--------------------------------------
void connect() {
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    String mqttClientId = "A";
    if (mqttClient.connect(mqttClientId.c_str(), mqttUser, mqttPassword)) {
      Serial.println("connected");
      mqttClient.subscribe(mqttTopicIn);
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" will try again in 5 seconds");
      delay(5000);
    }
  }
}
Servo foot_right;
Servo foot_left;
Servo leg_right;
Servo leg_left;

void setup() {
  Serial.begin(9600);

  setup_wifi();
  mqttClient.setServer(mqtt_server, mqtt_server_port);
  mqttClient.setCallback(callback);

  foot_right.attach(D4,500,2400);
  foot_left.attach(D3,500,2400);
  leg_right.attach(D2,500,2400);
  leg_left.attach(D1,500,2400);
}

void loop(){

   if (!mqttClient.connected()) {
    connect();
  }
 
  mqttClient.loop();

  leg_right.write(90);
  
}
