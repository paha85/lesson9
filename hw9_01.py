from time import sleep

class TrafficLight():
    colours = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Сейчас горит - {TrafficLight.colours[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()