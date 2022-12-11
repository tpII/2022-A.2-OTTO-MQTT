#include <Servo.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFiUdp.h>
#include "lib_otto.h"

//--------------------------------------
// configuracion
//--------------------------------------

#define PIE_DER D4
#define PIE_IZQ D3
#define PIERNA_DER D2
#define PIERNA_IZQ D1
#define TRIGGER D5 // ultrasonic sensor trigger pin
#define ECHO D6 // ultrasonic sensor echo pin

Otto otto;
Otto::function f;
int intValue=0;
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
  if (length >= 2) { //Transformo el mensaje a int
    payload[length] = '\0'; // Make payload a string by NULL terminating it.
    intValue = atoi((char *)payload);
    Serial.print(intValue);
  }
  // Obtengo la funcion del movimiento llamada por el mensaje
  f = otto.Otto::doActionsArray [intValue];
  // Invoco el movimiento
  (otto.*f) ();
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
  otto.init(PIERNA_IZQ, PIERNA_DER, PIE_IZQ,PIE_DER,TRIGGER,ECHO);
  otto.home(); //Posicion inicial
  delay(500);
  intValue=0;
    
  setup_wifi();
  mqttClient.setServer(mqtt_server, mqtt_server_port);
  mqttClient.setCallback(callback);
  // Seteo los pines del otto
  

}

void loop(){

   if (!mqttClient.connected()) {
    connect();
  }
 
  mqttClient.loop();

  // Si la ultima funcion invocada fue alguna de las que usan el ultrasonido
  // sigo invocando esta funcion, hasta que se invoque a otra.
  if (intValue >= 20){ 
    (otto.*f) ();
  }

  
}
