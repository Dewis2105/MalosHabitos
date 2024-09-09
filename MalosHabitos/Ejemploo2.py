def multisuma(multiplicando1, multiplicando2, sumando):
    resultado_multisuma = multiplicando1 * multiplicando2 + sumando
    return resultado_multisuma

if __name__=="__main__":
    multiplicando_1 = float(input("multiplicando 1: "))
    multiplicando_2 = float(input("multiplicando 2: "))
    sumando = float(input("sumando: "))
    resultado_final = multisuma(multiplicando_1, multiplicando_2, sumando)
    print(f" {multiplicando_1} x {multiplicando_2} + {sumando} = {resultado_final}")
