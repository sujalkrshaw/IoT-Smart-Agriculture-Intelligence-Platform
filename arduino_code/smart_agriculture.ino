// SMART AGRICULTURE SYSTEM
// ESP32 + Soil + Water + Pump

#define SOIL_PIN 34
#define WATER_PIN 4
#define PUMP_PIN 25

#define SOIL_THRESHOLD 2000
#define WATER_THRESHOLD 1000
#define TEMP_THRESHOLD 35

void setup() {

  Serial.begin(115200);

  pinMode(PUMP_PIN, OUTPUT);

  Serial.println("=================================");
  Serial.println(" SMART AGRICULTURE SYSTEM");
  Serial.println("=================================");
}

void loop() {

  // Simulated Temperature & Humidity
  float temperature = random(22, 40);
  float humidity = random(40, 90);

  int soil = analogRead(SOIL_PIN);
  int water = analogRead(WATER_PIN);

  if (soil < SOIL_THRESHOLD) {
    digitalWrite(PUMP_PIN, HIGH);
  } else {
    digitalWrite(PUMP_PIN, LOW);
  }

  Serial.println("\n===== SMART FARM REPORT =====");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Soil Moisture: ");
  Serial.println(soil);

  Serial.print("Water Level: ");
  Serial.println(water);

  if (soil < SOIL_THRESHOLD) {
    Serial.println("ALERT: Soil Dry");
    Serial.println("PUMP STATUS: ON");
  } else {
    Serial.println("PUMP STATUS: OFF");
  }

  if (water < WATER_THRESHOLD) {
    Serial.println("ALERT: Low Water Level");
  }

  if (temperature > TEMP_THRESHOLD) {
    Serial.println("ALERT: High Temperature");
  }

  delay(3000);
}