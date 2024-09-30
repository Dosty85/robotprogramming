from microbit import button_a, sleep, i2c

from cely_projekt import Konstanty, KalibracniFaktory, Robot

def zakladni_test_spusteni():

    min_rychlost = 0.6233437
    min_pwm_rozjezd = 57 # kalibrace vytiskne na konci pri "zrychluj"
    min_pwm_dojezd = 54 # kalibrace vytiskne na konci pri "zpomaluj"
    a = 25.4585241095727 # ziskej z excelu
    b = 41.1305893849997 # ziskej z excelu

    levy_faktor = KalibracniFaktory(min_rychlost, min_pwm_rozjezd, min_pwm_dojezd, a, b)

    min_rychlost = 0.7791749
    min_pwm_rozjezd = 57
    min_pwm_dojezd = 54
    a = 25.4604475451773
    b = 39.1618583300312

    pravy_faktor = KalibracniFaktory(min_rychlost, min_pwm_rozjezd, min_pwm_dojezd, a, b)

    robot = Robot(0.15, 0.067, levy_faktor, pravy_faktor, True)
    robot.inicializuj()
    robot.jed(0.067*Konstanty.PI, 0)

    while not button_a.was_pressed():
        sleep(5)
        robot.aktualizuj_se()

    robot.jed(0,0)

if __name__ =="__main__":
    zakladni_test_spusteni()

