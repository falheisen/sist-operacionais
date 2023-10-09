###############################################################################################################
##
## PCS-3446 - SISTEMAS OPERACIONAIS
## Alunos: Filipe Penna Ceravolo Soares (10774009) e Pier Luigi (XXXXXXX)
## Professor: Prof. Dr. João José Neto
## Objetivo: Simular o OS
## Ano: 2023
##
###############################################################################################################

import pandas as pd
from componentes.job import Job

if __name__ == "__main__":

    jobs = pd.read_csv('job_lists/teste1.csv')
    lista_jobs = []
    for i in range(len(jobs)):
        job = jobs.iloc[i]
        lista_jobs.append(Job(
            id=job.Job,
            chegada=job.InstanteChegada, 
            memoria=job.MemoriaOcupada, 
            duracao=job.DuracaoDoProcessamento, 
            entradas=job.Entradas, 
            saidas=job.Saidas
        ))
    print(lista_jobs[0])
    