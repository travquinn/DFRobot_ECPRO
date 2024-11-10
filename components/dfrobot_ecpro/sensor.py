import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, ads1115
from esphome.const import CONF_ID, UNIT_MICROSIEMENS_PER_CENTIMETER, ICON_FLASH

DEPENDENCIES = ['ads1115']

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent)

CONF_ADS1115_ID = 'ads1115_id'
CONF_ADS1115_MULTIPLEXER = 'ads1115_multiplexer'
CONF_ADS1115_GAIN = 'ads1115_gain'
CONF_TEMPERATURE = 'temperature'

CONFIG_SCHEMA = sensor.sensor_schema(
    DFRobotECProSensor,
    unit_of_measurement=UNIT_MICROSIEMENS_PER_CENTIMETER,
    icon=ICON_FLASH,
    accuracy_decimals=2
).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
    cv.Required(CONF_ADS1115_ID): cv.use_id(ads1115.ADS1115Component),
    cv.Required(CONF_ADS1115_MULTIPLEXER): cv.enum(ads1115.ADS1115_MULTIPLEXER_OPTIONS, upper=True),
    cv.Required(CONF_ADS1115_GAIN): cv.enum(ads1115.ADS1115_GAIN_OPTIONS, float=True),
    cv.Optional(CONF_TEMPERATURE, default=25.0): cv.float_,
}).extend(cv.polling_component_schema('60s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    ads = await cg.get_variable(config[CONF_ADS1115_ID])
    cg.add(var.set_ads1115(ads))
    cg.add(var.set_ads1115_multiplexer(config[CONF_ADS1115_MULTIPLEXER]))
    cg.add(var.set_ads1115_gain(config[CONF_ADS1115_GAIN]))
    cg.add(var.set_temperature(config[CONF_TEMPERATURE]))
