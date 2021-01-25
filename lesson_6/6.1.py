from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1

    def back_running(self):
        i = 1
        while i > -1:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 1:
                sleep(2)
            elif i == 0:
                sleep(7)
            i -= 1

    def running1(self):
        i = 1
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()
count = 0
while count < 3:
    TrafficLight.back_running()
    TrafficLight.running1()
    count += 1