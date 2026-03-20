import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_TYPE,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_POWER_FACTOR,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_EMPTY,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_MINUTE,
    UNIT_HERTZ,
    UNIT_WATT,
    UNIT_SECOND,
)


from . import ups_hid_ns, UpsHidComponent, CONF_UPS_HID_ID

DEPENDENCIES = ["ups_hid"]

UpsHidSensor = ups_hid_ns.class_("UpsHidSensor", sensor.Sensor, cg.Component)

SENSOR_TYPES = {
    "battery_level": {
        "unit": UNIT_PERCENT,
        "device_class": DEVICE_CLASS_BATTERY,
        "accuracy_decimals": 0,
    },
    "input_voltage": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 1,
    },
    "output_voltage": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 1,
    },
    "load_percent": {
        "unit": UNIT_PERCENT,
        "device_class": DEVICE_CLASS_POWER_FACTOR,
        "accuracy_decimals": 0,
    },
    "runtime": {
        "unit": UNIT_MINUTE,
        "device_class": DEVICE_CLASS_DURATION,
        "accuracy_decimals": 0,
    },
    "frequency": {
        "unit": UNIT_HERTZ,
        "accuracy_decimals": 1,
    },
    "battery_voltage": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 1,
    },
    "battery_voltage_nominal": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 0,
    },
    "input_voltage_nominal": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 0,
    },
    "input_transfer_low": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 0,
    },
    "input_transfer_high": {
        "unit": UNIT_VOLT,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "accuracy_decimals": 0,
    },
    "ups_realpower_nominal": {
        "unit": UNIT_WATT,
        "device_class": DEVICE_CLASS_POWER,
        "accuracy_decimals": 0,
    },
    "ups_delay_shutdown": {
        "unit": UNIT
