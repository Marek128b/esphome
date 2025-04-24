import esphome.codegen as cg
from esphome.components import display, light
import esphome.config_validation as cv
from esphome.const import (
    CONF_ADDRESSABLE_LIGHT_ID,
    CONF_ID,
    CONF_NUM_LEDS,
    CONF_INTENSITY,

)

addressable_light_ns = cg.esphome_ns.namespace("addressable_light")
AddressableLightDisplay = addressable_light_ns.class_(
    "AddressableLightDisplay", display.DisplayBuffer, cg.PollingComponent
)

CONFIG_SCHEMA = cv.All(
    display.BASIC_DISPLAY_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(AddressableLightDisplay),
            cv.Optional(CONF_NUM_LEDS,default=1): cv.int_range(min=1,max=1024),
            cv.Optional(CONF_INTENSITY): cv.int_range(min=0,max=255),
        }
    ),
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    wrapped_light = await cg.get_variable(config[CONF_ADDRESSABLE_LIGHT_ID])
    await display.register_display(var, config)
    cg.add(var.set_num_leds(config[CONF_NUM_LEDS]))

