#pragma once

#include "esphome.h"
#include "DFRobot_ECPRO.h"
#include "esphome/components/ads1115/ads1115.h"

namespace esphome {
namespace dfrobot_ecpro {

class DFRobotECProSensor : public sensor::Sensor, public PollingComponent {
 public:
  void set_ads1115(ads1115::ADS1115Component *ads1115) { ads1115_ = ads1115; }
  void set_multiplexer(ads1115::ADS1115Multiplexer multiplexer) { multiplexer_ = multiplexer; }
  void set_gain(ads1115::ADS1115Gain gain) { gain_ = gain; }

  void setup() override {
    ecpro_.begin();
  }

  void update() override {
    float voltage = ads1115_->request_measurement(multiplexer_, gain_);
    float ec = ecpro_.readEC(voltage);
    publish_state(ec);
  }

 protected:
  DFRobot_ECPRO ecpro_;
  ads1115::ADS1115Component *ads1115_;
  ads1115::ADS1115Multiplexer multiplexer_;
  ads1115::ADS1115Gain gain_;
};

}  // namespace dfrobot_ecpro
}  // namespace esphome
