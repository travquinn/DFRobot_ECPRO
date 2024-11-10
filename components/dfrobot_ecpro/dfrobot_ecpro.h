#pragma once

#include "esphome.h"
#include "DFRobot_ECPRO.h"
#include "esphome/components/ads1115/ads1115.h"

namespace esphome {
namespace dfrobot_ecpro {

class DFRobotECProSensor : public sensor::Sensor, public PollingComponent {
 public:
  DFRobotECProSensor() : PollingComponent(15000) {}

  void set_ads1115(ads1115::ADS1115Component *ads1115) { ads1115_ = ads1115; }
  void set_ads1115_multiplexer(ads1115::ADS1115Multiplexer multiplexer) { multiplexer_ = multiplexer; }
  void set_ads1115_gain(ads1115::ADS1115Gain gain) { gain_ = gain; }
  void set_temperature(float temperature) { temperature_ = temperature; }

  void setup() override {
    ecpro_ = new DFRobot_ECPRO();
  }

  void update() override {
    float voltage = ads1115_->request_measurement(multiplexer_, gain_, ADS1115_RESOLUTION_16_BIT);
    float ec = ecpro_->getEC_us_cm(voltage, temperature_);
    publish_state(ec);
  }

 protected:
  DFRobot_ECPRO *ecpro_;
  ads1115::ADS1115Component *ads1115_;
  ads1115::ADS1115Multiplexer multiplexer_;
  ads1115::ADS1115Gain gain_;
  float temperature_ = 25.0; // Default temperature if not set
};

}  // namespace dfrobot_ecpro
}  // namespace esphome
