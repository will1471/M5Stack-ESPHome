import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import (
    STATE_CLASS_MEASUREMENT,
    ICON_ARROW_EXPAND_VERTICAL,
)

CONF_I2C_ADDR = 0x57

DEPENDENCIES = ['i2c']

sonic_sensor_ns = cg.esphome_ns.namespace("sonic_i2c_sensor")
SonicI2C = sonic_sensor_ns.class_("SonicI2C",sensor.Sensor, i2c.I2CDevice, cg.PollingComponent)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        SonicI2C,
        unit_of_measurement="mm",
        icon=ICON_ARROW_EXPAND_VERTICAL,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    )
    .extend(cv.polling_component_schema("60s")
    .extend(i2c.i2c_device_schema(CONF_I2C_ADDR)))
)

async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    

    
