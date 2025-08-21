def falla_automovil():
    print("=== Sistema Experto Diagnóstico de Fallas en un Automóvil ===\n")
    print("Estimado usuario, responda con 'si' o 'no' las siguientes preguntas de acuerdo a las fallas que presente su automóvil.\n")

    bateria = input("¿El automóvil arranca? (si/no): ")
    luces = input("¿Las luces del tablero encienden? (si/no): ")
    combustible = input("¿El automóvil se apaga al acelerar? (si/no): ")
    escape = input("¿El automóvil tiene humo negro por el escape? (si/no): ")
    humo_blanco = input("¿El automóvil tiene humo blanco constante? (si/no): ")

    if bateria == "no" and luces == "no":
        print("Posible falla: batería descargada")

    elif bateria == "no" and luces == "si":
        print("Posible falla: motor de arranque")

    elif combustible == "si":
        print("Posible falla: problema en el suministro de combustible")

    elif escape == "si":
        print("Posible falla: mezcla rica de combustible")

    elif humo_blanco == "si":
        print("Posible falla: falla en la junta de culata")

    else:
        print("No se puede determinar la falla con la información proporcionada")


if __name__ == "__main__":
    falla_automovil()
