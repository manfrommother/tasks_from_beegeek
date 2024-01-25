class Gun():

    def __init__(self):
        self.shoot_counter = 1

    def shoot(self):
        if self.shoot_counter % 2 != 0:
            print('paf')
        else:
            print('pif')
        self.shoot_counter += 1


gun = Gun()
gun.shoot()
gun.shoot()