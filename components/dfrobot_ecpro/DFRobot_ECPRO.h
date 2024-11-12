/*!
  * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  * @licence     The MIT License (MIT)
  * @author      PengKaixing(kaixing.peng@dfrobot.com)
  * @version     V0.1
  * @date        2021-05-31
  * @get         from https://www.dfrobot.com
  * @url         https://github.com/dfrobot/DFRobot_ECPRO
  */

#ifndef __DFRobot_ECPRO_H__
#define __DFRobot_ECPRO_H__

#if ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif

#include "EEPROM.h"

#define KVALUEADDR 0x0A //the start address of the K value stored in the EEPROM
#define RES2 820.0
#define ECREF 200.0
#define GDIFF (30/1.8)
#define VR0  0.223
#define G0  2
#define I  (1.24 / 10000)

#define EEPROM_write(address, p) {int i = 0; byte *pp = (byte*)&(p);for(; i < sizeof(p); i++) EEPROM.write(address+i, pp[i]);}
#define EEPROM_read(address, p)  {int i = 0; byte *pp = (byte*)&(p);for(; i < sizeof(p); i++) pp[i]=EEPROM.read(address+i);}

class DFRobot_ECPRO
{
  public:
    DFRobot_ECPRO();
    DFRobot_ECPRO(float calibration);
    ~DFRobot_ECPRO(){};
    /**
     * @brief Get the EC value in us/cm (with temperature calibration)
     * @param voltage: ADC voltage value
     * @return EC value in us/cm
     */
    float getEC_us_cm(float voltage);

    /**
     * @brief Get the EC value in us/cm (without temperature calibration)
     * @param voltage: ADC voltage value
     * @param temperature: Solution temperature
     * @return EC value in us/cm
     */
    float getEC_us_cm(float voltage, float temperature);

    /**
     * @brief Set calibration value and save it permanently in EEPROM
     * @param calibration: Calibration value
     * @return Success or failure
     */
    bool setCalibration(float calibration);

    /**
     * @brief Get calibration value
     * @return Calibration value
     */
    float getCalibration();

    /**
     * @brief Calibrate (with built-in reference k value of 1)
     * @param voltage: EC sensor output voltage
     * @return Calibrated value
     */
    float calibrate(float voltage);

    /**
     * @brief Calibrate
     * @param voltage: EC sensor output voltage
     * @param reference: Reference k value (0.5 < k < 1.5)
     * @return Calibrated value
     */
    float calibrate(float voltage, float reference); 
  private:
    float _kvalue;
};

class DFRobot_ECPRO_PT1000
{
  public:
    DFRobot_ECPRO_PT1000(){};
    ~DFRobot_ECPRO_PT1000(){};
    /**
     * @brief Convert voltage to temperature in Celsius
     * @param voltage: PT1000 sensor output voltage
     * @return Temperature in Celsius
     */
    float convVoltagetoTemperature_C(float voltage);
};

#endif // __DFRobot_ECPRO_H__
