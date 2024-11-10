import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, ads1115
from esphome.const import CONF_ID, UNIT_MICROSIEMENS_PER_CENTIMETER, ICON_FLASH

DEPENDENCIES = ['ads1115']

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent)

CONF_ADS1115_ID = 'ads1115_id'
CONF_MULTIPLEXER = 'multiplexer'
CONF_GAIN = 'gain'

CONFIG_SCHEMA = sensor.sensor_schema(
    DFRobotECProSensor,
    unit_of_measurement=UNIT_MICROSIEMENS_PER_CENTIMETER,
    icon=ICON_FLASH,
    accuracy_decimals=2
).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
    cv.Required(CONF_ADS1115_ID): cv.use_id(ads1115.ADS1115Component),
    cv.Required(CONF_MULTIPLEXER): cv.enum(ads1115.ADS1115_MULTIPLEXER_OPTIONS, upper=True),
    cv.Required(CONF_GAIN): cv.enum(ads1115.ADS1115_GAIN_OPTIONS, float=True),
}).extend(cv.polling_component_schema('60s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    ads = await cg.get_variable(config[CONF_ADS1115_ID])
    cg.add(var.set_ads1115(ads))
    cg.add(var.set_multiplexer(config[CONF_MULTIPLEXER]))
    cg.add(var.set_gain(config[CONF_GAIN]))
