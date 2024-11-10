#pragma once

#include "esphome.h"
#include "DFRobot_ECPRO.h"

class DFRobotECProSensor : public PollingComponent, public Sensor {
 public:
  DFRobot_ECPRO ecpro;

  DFRobotECProSensor() : PollingComponent(15000) {}

  void setup() override {
    // Initialize the sensor
    ecpro.begin();
  }

  void update() override {
    // Read the sensor data and publish it
    float ec = ecpro.readEC();
    if (!isnan(ec)) {
      publish_state(ec);
    } else {
      ESP_LOGW("custom", "Failed to read EC value");
    }
  }
};
