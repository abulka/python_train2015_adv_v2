from lib.light_calculator import calc_speed_of_light

def beamline_calc(a,b):
    return a+b+calc_speed_of_light()
