#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#define BLYNK_TEMPLATE_ID "TMPL2Xm2_nzA3"
#define BLYNK_TEMPLATE_NAME "ADC Leds"
#define BLYNK_AUTH_TOKEN 

// Enter your Auth token
char auth[] = "He7yNYtNRuUE61RplFxQfxh_36PwLrPZ";

//Enter your WIFI SSID and password
char ssid[] = "FAMILIALOMBANA";
char pass[] = "GL0MB4N463";

void setup(){
  // Debug console
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
}

void loop(){
  Blynk.run();
}