try:
    vlan = int(input("Ingrese el número de VLAN: "))

    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} corresponde al rango normal.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} corresponde al rango extendido.")
    else:
        print(f"La VLAN {vlan} no es válida.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
