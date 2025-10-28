print("=== MINI IA DIAGNÓSTICA ===\n")

# NÍVEL 1
febre = input("O paciente apresenta febre? (sim/não): ")

if febre == "sim":
    # NÍVEL 2
    dor_cabeca = input("O paciente está com dor de cabeça intensa? (sim/não): ")
    
    if dor_cabeca == "sim":
        # NÍVEL 3
        dor_corpo = input("Há dor no corpo e fadiga? (sim/não): ")
        
        if dor_corpo == "sim":
            # NÍVEL 4
            tosse = input("Está com tosse seca? (sim/não): ")
            
            if tosse == "sim":
                # NÍVEL 5
                respirar = input("Sente dificuldade para respirar? (sim/não): ")
                
                if respirar == "sim":
                    print("\nDiagnóstico: Pode ser COVID-19")
                    print("Recomendação: Procure atendimento médico e faça o teste.")
                else:
                    print("\nDiagnóstico: Pode ser Gripe")
                    print("Recomendação: Descanse e beba bastante água.")
            else:
                print("\nDiagnóstico: Pode ser Dengue")
                print("Recomendação: Procure atendimento médico e evite aspirina.")
        else:
            print("\nDiagnóstico: Pode ser Enxaqueca com febre")
            print("Recomendação: Evite barulho e procure um médico se persistir.")
    else:
        print("\nDiagnóstico: Pode ser Infecção leve")
        print("Recomendação: Observe os sintomas e mantenha-se hidratado.")
        
else:
    # NÍVEL 2
    tosse = input("O paciente está com tosse ou espirros? (sim/não): ")
    
    if tosse == "sim":
        # NÍVEL 3
        coceira = input("Apresenta coceira na garganta? (sim/não): ")
        
        if coceira == "sim":
            # NÍVEL 4
            nariz = input("O nariz está escorrendo? (sim/não): ")
            
            if nariz == "sim":
                # NÍVEL 5
                corpo = input("Sente dores no corpo? (sim/não): ")
                
                if corpo == "sim":
                    print("\nDiagnóstico: Pode ser Resfriado Forte")
                    print("Recomendação: Descanse e evite friagem.")
                else:
                    print("\nDiagnóstico: Pode ser Alergia Respiratória")
                    print("Recomendação: Evite poeira e produtos com cheiro forte.")
            else:
                print("\nDiagnóstico: Pode ser Irritação leve na garganta")
                print("Recomendação: Beba água morna e evite gelados.")
        else:
            print("\nDiagnóstico: Pode ser Tosse passageira")
            print("Recomendação: Observe se o sintoma piora nos próximos dias.")
    else:
        print("\nDiagnóstico: Nenhum sintoma relevante")
        print("Recomendação: Continue com hábitos saudáveis e boa alimentação.")
