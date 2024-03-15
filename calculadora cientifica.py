from sympy import symbols, sin, cos, tan, sqrt, log, exp, pi, parse_expr

def calculadora_cientifica():
    x = symbols('x')

    print("Calculadora Científica")
    print("Operaciones disponibles: +, -, *, /, sin, cos, tan, sqrt, log, exp, pi")
    print("Ingrese 'salir' para salir")

    while True:
        expresion = input("Ingrese una expresión: ")

        if expresion.lower() == 'salir':
            print("Saliendo de la calculadora.")
            break

        try:
            expresion_parsed = parse_expr(expresion)
            resultado = expresion_parsed.evalf(subs={x: 0})  # Para evaluar en x=0, puedes cambiar el valor según tus necesidades
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculadora_cientifica()