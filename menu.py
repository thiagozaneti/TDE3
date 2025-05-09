def determinante_1x1_menu():
    valor = float(input("Digite o único valor da matriz 1x1: "))
    print(f"Determinante: {valor}")

def determinante_2x2_menu():
    print("Digite os valores da matriz 2x2:")
    a11 = float(input("a11: "))
    a12 = float(input("a12: "))
    a21 = float(input("a21: "))
    a22 = float(input("a22: "))
    determinante = (a11 * a22) - (a12 * a21)
    print(f"Determinante: {determinante}")

def determinante_3x3_menu():
    print("Digite os valores da matriz 3x3:")
    a11 = float(input("a11: "))
    a12 = float(input("a12: "))
    a13 = float(input("a13: "))
    a21 = float(input("a21: "))
    a22 = float(input("a22: "))
    a23 = float(input("a23: "))
    a31 = float(input("a31: "))
    a32 = float(input("a32: "))
    a33 = float(input("a33: "))
