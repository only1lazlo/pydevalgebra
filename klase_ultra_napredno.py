class KlasaPero:
    def __init__(self):
        pass

    def luda_funkcija(self, *args, **kwargs):
        """ovo je ludi i napredni primjer"""
        print(args)
        print(kwargs)

pero = KlasaPero()

pero.luda_funkcija("12", ime="Stipe")
pero.luda_funkcija("12", 1, 79, "Pero", ime="Stipe", prezime="Krešo")
pero.luda_funkcija()