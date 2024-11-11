import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, ads1115
from esphome.const import CONF_ID

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(DFRobotECProSensor).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
    cv.Required('ads1115_id'): cv.use_id(ads1115.ADS1115Component),
    cv.Required('ads1115_multiplexer'): cv.enum(ads1115.ADS1115_MULTIPLEXER_OPTIONS, upper=True),
    cv.Required('ads1115_gain'): cv.enum(ads1115.ADS1115_GAIN_OPTIONS, float=True),
    cv.Optional('temperature', default=25.0): cv.float_,
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    ads = await cg.get_variable(config['ads1115_id'])
    cg.add(var.set_ads1115(ads))
    cg.add(var.set_multiplexer(config['ads1115_multiplexer']))
    cg.add(var.set_gain(config['ads1115_gain']))
    cg.add(var.set_temperature(config['temperature']))
