
inventario = {
    "manzanas": 5,
    "platanos": 10,
    "naranjas": 7,

}

# sumar platanos
inventario["platanos"] += 5

# ver inventario actualizado

for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad}")