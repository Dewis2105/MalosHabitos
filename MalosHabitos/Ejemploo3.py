def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

if __name__ == "__main__":
    # Solicitar datos del rectángulo
    base_rectangulo = float(input("Base del rectángulo: "))
    altura_rectangulo = float(input("Altura del rectángulo: "))
    area_rect = area_rectangulo(base_rectangulo, altura_rectangulo)
    print(f"Área del rectángulo: {area_rect}")

    # Solicitar datos del triángulo
    base_triangulo = float(input("Base del triángulo: "))
    altura_triangulo = float(input("Altura del triángulo: "))
    area_tri = area_triangulo(base_triangulo, altura_triangulo)
    print(f"Área del triángulo: {area_tri}")
