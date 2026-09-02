tru_dict = {
            "Que es Toys R Us": "una jugueteria de EE.UU que es muy popular al rededor del mundo",
            "Toys R Us desaparecio": "En 2017 la marca se declaro bancarrota y cerraron todas sus tiendas en EE.UU y Reino Unido pero en 2019 la marca regreso en centros comerciales y unos años más tarde abrieron en tiendas Macys y en otros paises como Mexico, España, Venezuela, Ecuador y muchos más",
            }

word = input("Escribe una duda sobre Toys R Us (¡con mayúsculas!): ")

if word in tru_dict.keys():
    print(tru_dict[word])
else:
    print("No encontramos eso")
