def calculo_bloco_serie(disponibilidades):
    disp_bloco = 1
    for d in disponibilidades:
        disp_bloco = disp_bloco * d
    return disp_bloco

def calculo_bloco_paralelo(disponibilidades):
    indisponibilidades = []
    indisponibilidade_sis = 1
    for d in disponibilidades:
        indisp_comp = 1 - d
        indisponibilidades.append(indisp_comp)
    for i in indisponibilidades:
        indisponibilidade_sis = indisponibilidade_sis * i
    disponibilidade_sis = 1 - indisponibilidade_sis
    return disponibilidade_sis

def calcula_disp_sistema(disponibilidades_blocos):
    disp_sistema = 1
    for d in disponibilidades_blocos:
        disp_sistema = disp_sistema * d
    return disp_sistema

def main():
    disponibilidades_digitadas = []
    disponibilidades_blocos = []
    disp_sistema = 0
    while(1):
        bloco = str(input("Digite o tipo do bloco (dê enter em um valor vazio para parar o programa e calcular a disponibilidade do sistema): "))
        if bloco == "":
            break
        while(1):
            disp = float(input("Digite a disponibilidade (digite -1 para parar de digitar disponibilidades):"))
            if disp == -1:
                if bloco.upper() == "SERIE": 
                    disp_cal = calculo_bloco_serie(disponibilidades_digitadas)
                    disponibilidades_blocos.append(disp_cal)
                    disponibilidades_digitadas = []
                    break
                else:
                    disp_cal = calculo_bloco_paralelo(disponibilidades_digitadas)
                    disponibilidades_blocos.append(disp_cal)
                    disponibilidades_digitadas = []
                    break 
            else:
                disponibilidades_digitadas.append(disp)
            
    disp_sistema = calcula_disp_sistema(disponibilidades_blocos)
    print('A disponibilidade do sistema foi de {}'.format(disp_sistema))
    
main()
