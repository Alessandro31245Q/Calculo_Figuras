import streamlit as st
import math

def calcular_area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def calcular_area_perimetro_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def calcular_area_perimetro_triangulo(base, altura):
    area = 0.5 * base * altura
    # En un triángulo, el perímetro depende del tipo específico de triángulo
    perimetro = 3 * base  # Ejemplo: Perímetro de un triángulo equilátero
    return area, perimetro

def calcular_area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def calcular_volumen_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    volumen = area_base * altura
    return volumen,area_base

def calcular_volumen_cono(radio, altura):
    area_base = math.pi * radio ** 2
    volumen = (1 / 3) * area_base * altura
    return volumen, area_base

def calcular_volumen_esfera(radio):
    volumen = (4 / 3) * math.pi * radio ** 3
    return volumen

def calcular_volumen_paralelepipedo(largo, ancho, altura):
    volumen = largo * ancho * altura
    return volumen


# Página principal
def main():
    st.title("Calculadora de Área, Perímetro y Volumen")

    forma_seleccionada = st.radio("Selecciona una forma:", ["Cuadrado", "Círculo", "Triángulo", "Rectángulo", "Cilindro",
                                                            "Cono", "Esfera", "Paralelepípedo"])

    if forma_seleccionada == "Cuadrado":
        lado_cuadrado = st.number_input("Ingresa el lado del cuadrado:", min_value=0.0)
        if st.button("Calcular"):
            area, perimetro = calcular_area_perimetro_cuadrado(lado_cuadrado)
            st.write(f"Área del cuadrado: {area}")
            st.write(f"Perímetro del cuadrado: {perimetro}")

    elif forma_seleccionada == "Círculo":
        radio_circulo = st.number_input("Ingresa el radio del círculo:", min_value=0.0)
        if st.button("Calcular"):
            area, perimetro = calcular_area_perimetro_circulo(radio_circulo)
            st.write(f"Área del círculo: {area}")
            st.write(f"Perímetro del círculo: {perimetro}")

    elif forma_seleccionada == "Triángulo":
        base_triangulo = st.number_input("Ingresa la base del triángulo:", min_value=0.0)
        altura_triangulo = st.number_input("Ingresa la altura del triángulo:", min_value=0.0)
        if st.button("Calcular"):
            area, perimetro = calcular_area_perimetro_triangulo(base_triangulo, altura_triangulo)
            st.write(f"Área del triángulo: {area}")
            st.write(f"Perímetro del triángulo: {perimetro}")

    elif forma_seleccionada == "Rectángulo":
        base_rectangulo = st.number_input("Ingresa la base del rectángulo:", min_value=0.0)
        altura_rectangulo = st.number_input("Ingresa la altura del rectángulo:", min_value=0.0)
        if st.button("Calcular"):
            area, perimetro = calcular_area_perimetro_rectangulo(base_rectangulo, altura_rectangulo)
            st.write(f"Área del rectángulo: {area}")
            st.write(f"Perímetro del rectángulo: {perimetro}")

    elif forma_seleccionada == "Cilindro":
        radio_cilindro = st.number_input("Ingresa el radio del cilindro:", min_value=0.0)
        altura_cilindro = st.number_input("Ingresa la altura del cilindro:", min_value=0.0)
        if st.button("Calcular"):
            volumen_cilindro,area = calcular_volumen_cilindro(radio_cilindro, altura_cilindro)
            st.write(f"Area de la base del cilindro: {area}")
            st.write(f"Volumen del cilindro: {volumen_cilindro}")

    elif forma_seleccionada == "Cono":
        radio_cono = st.number_input("Ingresa el radio del cono:", min_value=0.0)
        altura_cono = st.number_input("Ingresa la altura del cono:", min_value=0.0)
        if st.button("Calcular"):
            volumen_cono, area_base_cono = calcular_volumen_cono(radio_cono, altura_cono)
            st.write(f"Área de la base del cono: {area_base_cono}")
            st.write(f"Volumen del cono: {volumen_cono}")

    elif forma_seleccionada == "Esfera":
        radio_esfera = st.number_input("Ingresa el radio de la esfera:", min_value=0.0)
        if st.button("Calcular"):
            volumen_esfera = calcular_volumen_esfera(radio_esfera)
            st.write(f"Volumen de la esfera: {volumen_esfera}")

    elif forma_seleccionada == "Paralelepípedo":
        largo_paralelepipedo = st.number_input("Ingresa el largo del paralelepípedo:", min_value=0.0)
        ancho_paralelepipedo = st.number_input("Ingresa el ancho del paralelepípedo:", min_value=0.0)
        altura_paralelepipedo = st.number_input("Ingresa la altura del paralelepípedo:", min_value=0.0)
        if st.button("Calcular"):
            volumen_paralelepipedo = calcular_volumen_paralelepipedo(largo_paralelepipedo, ancho_paralelepipedo, altura_paralelepipedo)
            st.write(f"Volumen del paralelepípedo: {volumen_paralelepipedo}")




if __name__ == "__main__":
    main()
