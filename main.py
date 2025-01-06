from limpeza import limpar_prefetch, limpar_recent, limpar_temp, limpar_temp_2

def main():
    # Defina aqui se cada limpeza deve ocorrer
    deve_acontecer_prefetch = True    # Altere para False para desativar
    deve_acontecer_recent = True     
    deve_acontecer_temp = True        
    deve_acontecer_temp_2 = True      

    # Chamar as funções de limpeza com base nas variáveis definidas
    limpar_prefetch(deve_acontecer_prefetch)
    limpar_recent(deve_acontecer_recent)
    limpar_temp(deve_acontecer_temp)
    limpar_temp_2(deve_acontecer_temp_2)

if __name__ == "__main__":
    main()