print(" O condutor é PCD? S para Sim e N para não: ")
condutor = input()

if (condutor == "s"):
    print(".......................................");
    print("")
    print("Olá você pode pode transitar livremente")
    print("")
    print(".......................................")
else:
    print(" Escolha o veiculo: C para carro ou  M para moto: ")
    tipoVeiculo = input()
    finalPlaca = int(input("Qual o final da placa: de 0 a 9: "))
    print("")
    print(".......................................")

    if tipoVeiculo == "c":
        print("Seu veiculo é um: carro")
        if finalPlaca == 1:
            print("Seu rodizio é: Segunda e Quarta-feira ")
        else:
            if finalPlaca == 2:
                print("Seu rodizio é: Segunda e Quarta-feira ")
            else:
                if finalPlaca == 3:
                    print("Seu rodizio é: Terça e Quinta-feira")
                else:
                    if finalPlaca == 4:
                        print("Seu rodizio é: Terça e Quinta-feira")
                    else:
                        if finalPlaca == 5:
                            print("Seu rodizio é: Quarta e Sexta-feira")
                        else:
                            if finalPlaca == 6:
                                print("Seu rodizio é: Quarta e Sexta-feira")
                            else:
                                if finalPlaca == 7:
                                    print("Seu rodizio é: Segunda e Quinta-feira")
                                else:
                                    if finalPlaca == 8:
                                        print("Seu rodizio é: Segunda e Quinta-feira")
                                    else:
                                        if finalPlaca == 9:
                                            print("Seu rodizio é: Terça e Sexta-feira")
                                        else:
                                            if finalPlaca == 0:
                                                print("Seu rodizio é: Terça e Sexta-feira")
                                            else:
                                                print("Puts! Vc digitou a placa errada")
    else:

        if tipoVeiculo == "m":
            print("Seu veiculo é uma: moto")
        if finalPlaca == 1:
            print("Seu rodizio é: Segunda-feira ")
        else:
            if finalPlaca == 2:
                print("Seu rodizio é: Segunda-feira ")
            else:
                if finalPlaca == 3:
                  print("Seu rodizio é: Terça-feira")
                else:
                    if finalPlaca == 4:
                       print("Seu rodizio é: Terça-feira")
                    else:
                        if finalPlaca == 5:
                            print("Seu rodizio é: Quarta-feira")
                        else:
                            if finalPlaca == 6:
                                print("Seu rodizio é: Quarta-feira")
                            else:
                                if finalPlaca == 7:
                                    print("Seu rodizio é: Quinta-feira")
                                else:
                                    if finalPlaca == 8:
                                        print("Seu rodizio é: Quinta-feira")
                                    else:
                                        if finalPlaca == 9:
                                            print("Seu rodizio é: Sexta-feira")
                                        else:
                                            if finalPlaca == 0:
                                                print("Seu rodizio é: Sexta-feira")
                                            else:
                                                print("Puts! Vc digitou a placa errada")