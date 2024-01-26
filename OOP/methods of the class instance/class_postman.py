class Postman():

    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apart):
        self.delivery_data.append((street, house, apart))

    def get_houses_for_street(self, street):
        dict_keys = {}.fromkeys([i[1] for i in self.delivery_data if i[0] == street])
        return list(dict_keys.keys())
    
    def get_flats_for_house(self, street, house):
        dict_keys = {}.fromkeys([i[2] for i in self.delivery_data if i[0] == street and i[1] == house])
        return list(dict_keys.keys())
    

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))

