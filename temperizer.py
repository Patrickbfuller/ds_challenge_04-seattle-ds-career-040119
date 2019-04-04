"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temp_c):
    """Convert Celsius to Fahrenheit."""
    temp_f = (9/5) * temp_c + 32
    return temp_f

def convert_c_to_k(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

def convert_f_to_k(temp_f):
    temp_c = convert_f_to_c(temp_f)
    temp_k = convert_c_to_k(temp_c)
    return temp_k

def convert_k_to_c(temp_k):
    temp_c = temp_k -273.15
    return temp_c

def convert_k_to_f(temp_k):
    temp_c = temp_k -273.15
    temp_f = convert_c_to_f(temp_c)
    return temp_f