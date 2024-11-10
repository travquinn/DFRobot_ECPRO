import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, ads1115
from esphome.const import CONF_ID

DEPENDENCIES = ['ads1115']

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent)

CONF_ADS1115_ID = 'ads1115_id'

CONFIG_SCHEMA = sensor.sensor_schema(DFRobotECProSensor).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
    cv.Required(CONF_ADS1115_ID): cv.use_id(ads1115.ADS1115Component),
}).extend(cv.polling_component_schema('60s'))

async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)

    ads = await cg.get_variable(config[CONF_ADS1115_ID])
    cg.add(var.set_ads1115(ads))
