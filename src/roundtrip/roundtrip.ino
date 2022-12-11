#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFiUdp.h>


//--------------------------------------
// configuracion
//--------------------------------------



const char* ssid = "Otto";             // Parametros del AP
const char* password = "12345678";     // 
const char* mqtt_server = "192.168.0.200"; //Parametros del broker MQTT
const uint16_t mqtt_server_port = 1883;    //
const char* mqttUser = "Otto";             //
const char* mqttPassword = "DefaultOtto";  //
const char* mqttTopicIn = "otto";          //
const char* mqttTopicOut = "otto-out";     //


WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);


//--------------------------------------
// funcion para setear wifi llamada una sola vez
//--------------------------------------
void setup_wifi() {

  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected");
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
  // Confirmo que recibi el mensaje, enviando otro mensaje al broker
  mqttClient.publish(mqttTopicOut,"Recibido");

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

void setup() {
  
  Serial.begin(9600);
  setup_wifi();
  mqttClient.setServer(mqtt_server, mqtt_server_port);
  mqttClient.setCallback(callback);

}

void loop(){

   if (!mqttClient.connected()) {
    connect();
  }
 
  mqttClient.loop();

}