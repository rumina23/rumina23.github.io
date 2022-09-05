from devices2 import MobilePhone



class MobileColour(MobilePhone):

    def __init__(self, phoneColour, phoneMake, phoneDesc, phoneModel, phonePrice):

        super().__init__(phoneMake, phoneDesc, phoneModel, phonePrice)

        self.pColour = phoneColour



# mob1 = MobilePhone.MobileStorage("5TB")

# print(f" The storage size is {mob1.memoryCard}")



phoneA = MobileColour("Blue", "HTC", "Touchscreen", "One", 234.56)



print(f"{phoneA.pColour, phoneA.make, phoneA.description, phoneA.model, phoneA.price}")