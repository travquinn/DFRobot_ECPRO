import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, ads1115
from esphome.const import CONF_ID, UNIT_MICROSIEMENS_PER_CENTIMETER, ICON_FLASH, CONF_UPDATE_INTERVAL

DEPENDENCIES = ['ads1115']

dfrobot_ecpro_ns = cg.esphome_ns.namespace('dfrobot_ecpro')
DFRobotECProSensor = dfrobot_ecpro_ns.class_('DFRobotECProSensor', sensor.Sensor, cg.PollingComponent)

CONF_ADS1115_ID = 'ads1115_id'
CONF_ADS1115_MULTIPLEXER = 'ads1115_multiplexer'
CONF_ADS1115_GAIN = 'ads1115_gain'
CONF_TEMPERATURE = 'temperature'

# Define the multiplexer options
ADS1115_MULTIPLEXER_OPTIONS = {
    "A0_GND": 0b100,
    "A1_GND": 0b101,
    "A2_GND": 0b110,
    "A3_GND": 0b111,
    "A0_A1": 0b000,
    "A0_A3": 0b001,
    "A1_A3": 0b010,
    "A2_A3": 0b011,
}

# Define the gain options
ADS1115_GAIN_OPTIONS = {
    6.144: 0b000,
    4.096: 0b001,
    2.048: 0b010,
    1.024: 0b011,
    0.512: 0b100,
    0.256: 0b101,
}

CONFIG_SCHEMA = sensor.sensor_schema(
    DFRobotECProSensor,
    unit_of_measurement=UNIT_MICROSIEMENS_PER_CENTIMETER,
    icon=ICON_FLASH,
    accuracy_decimals=2
).extend({
    cv.GenerateID(): cv.declare_id(DFRobotECProSensor),
    cv.Required(CONF_ADS1115_ID): cv.use_id(ads1115.ADS1115Component),
    cv.Required(CONF_ADS1115_MULTIPLEXER): cv.enum(ads1115.ADS1115_MULTIPLEXER_OPTIONS, upper=True),
    cv.Required(CONF_ADS1115_GAIN): cv.enum(ads1115.ADS1115_GAIN_OPTIONS, upper=True),
    cv.Optional(CONF_TEMPERATURE, default=25.0): cv.float_,
    cv.Optional(CONF_UPDATE_INTERVAL, default="60s"): cv.update_interval,
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    ads = await cg.get_variable(config[CONF_ADS1115_ID])
    cg.add(var.set_ads1115(ads))
    cg.add(var.set_ads1115_multiplexer(config[CONF_ADS1115_MULTIPLEXER]))
    cg.add(var.set_ads1115_gain(config[CONF_ADS1115_GAIN]))
    cg.add(var.set_temperature(config[CONF_TEMPERATURE]))
    cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL]))
