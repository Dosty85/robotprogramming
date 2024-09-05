from microbit import i2c
from microbit import sleep
from microbit import pin19
from microbit import pin20
from microbit import pin14
from microbit import pin15
from microbit import button_a
from microbit import *

i2c.init(freq=400000, sda=pin20, scl=pin19)
i2c.write(0x70, b'\x00\x01')
i2c.write(0x70, b'\xE8\xAA')

def jed(dopredna_rychlost, rotace):
    d = 0.074  # tuto hodnotu si musite zmerit na robotovi, zadejte to v m
    v_l = dopredna_rychlost - d * rotace   # TODO vypocitejte dle prednasky 6
    v_r = dopredna_rychlost + d * rotace  # TODO vypocitejte dle prednasky 6

    zastav()

    if v_l < -255 or v_l > 255:
        return -1

    if v_r < -255 or v_r > 255:
        return -1

    if(v_l <= 0):
        i2c.write(0x70, b'\x02' + bytes([abs(int(v_l))]))
    else:
        i2c.write(0x70, b'\x03' + bytes([abs(int(v_l))]))

    if(v_r <= 0):
        i2c.write(0x70, b'\x04' + bytes([abs(int(v_r))]))
    else:
        i2c.write(0x70, b'\x05' + bytes([abs(int(v_r))]))

def zastav():
    i2c.write(0x70, b'\x02' + bytes([0]))
    i2c.write(0x70, b'\x03' + bytes([0]))
    i2c.write(0x70, b'\x04' + bytes([0]))
    i2c.write(0x70, b'\x05' + bytes([0]))

def enkoder_signal(jmeno_enkoderu):
    if jmeno_enkoderu == "pravy_enkoder":
        return int(pin15.read_digital())
    elif jmeno_enkoderu == "levy_enkoder":
        return int(pin14.read_digital())
    else:
        print("Zadali jste nepodporovane jmeno")
        return -1

if __name__ == "__main__":
    zastav()
    jed(255, 0)
    while not button_a.was_pressed():
        data_enkoderu = enkoder_signal("pravy_enkoder")
        data_enkoderu2 = enkoder_signal("levy_enkoder")
        img = Image(("00000" if data_enkoderu == 0 else "99999") + ":" +
            "00000:" +
            "00000:" +
            "00000:" +
            ("00000" if data_enkoderu2 == 0 else "99999") )
        print(img)
        display.show(img)
        sleep(1)
        print(data_enkoderu,data_enkoderu2)
    #sleep(1000)
    zastav()
    #sleep(1000)
    #jed(0, 1350)
    #sleep(1000)
    #zastav()




#if __name__ == "__main__":

#    while not button_a.was_pressed():
#        data_enkoderu = enkoder_signal("levy_enkoder")
#        if data_enkoderu == 1:
#            print("levy enkoder vidi")
#        elif data_enkoderu == 0:
#            print("levy enkoder nevidi")
#        else:
#            print("jsem tululum a upsala jsem se nekde v nazvu enkoderu :)")
#        sleep(100)
