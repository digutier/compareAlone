import logging
logging.basicConfig(filename="compareAloneLog.log", level=logging.INFO, format='%(asctime)s %(message)s')

def compareStrings(a, b):
    if (len(b) > len(a)):
        print("La cadena de caracteres más larga es:",b)
        logging.info("Se imprime el resultado esperado.")

    elif (len(a) > len(b)):
        print("La cadena de caracteres más larga es:",a)
        logging.info("Se imprime el resultado esperado.")

    else:
        print("Ambas palabras tienen el mismo largo.")
        logging.info("Se imprime el resultado esperado.")


x = input("Ingresa la primera cadena de caracteres:")
logging.info("La asignación de la cadena de caracteres se ha realizado con éxito.")
y = input("Ingresa la segunda cadena de caracteres:")
logging.info("La asignación de la cadena de caracteres se ha realizado con éxito.")

try:
    compareStrings(x,y)

except NameError:
    print("ERROR: Ambas variables deben estar definidas.")
    logging.error("ERROR: Ambas variables deben estar definidas.")

except TypeError:
    print("ERROR: Ambas variables deben ser del tipo string.")
    logging.error("ERROR: Ambas variables deben ser del tipo string.")