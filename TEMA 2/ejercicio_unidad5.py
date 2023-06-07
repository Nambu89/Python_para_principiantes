smallest = None
largest = None

while True:
    value = input("Ingrese un número o 'fin' para terminar: ")
    if value.lower() == 'fin':
        break
    try:
        value = int(value)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero o 'fin' para terminar.")
        continue
    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value

if smallest is not None and largest is not None:
    print('Mayor valor: ', largest, 'Menor valor: ', smallest)
else:
    print('No se ingresó ningún número.')
