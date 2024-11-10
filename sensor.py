import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import CONF_ID, UNIT_MICROSIEMENS_PER_CENTIMETER, ICON_FLASH

DEPENDENCIES = ['i2c']

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = sensor.sensor_schema(
    DFRobotECProSensor,
    unit_of_measurement=UNIT_MICROSIEMENS_PER_CENTIMETER,
    icon=ICON_FLASH,
    accuracy_decimals=2
).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
}).extend(cv.polling_component_schema('60s')).extend(i2c.i2c_device_schema(0x64))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    await sensor.register_sensor(var, config)
