# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from datetime import date
today = date.today()


# variables archivo

url_result = '../data/result.csv'
url_consoles = '../data/consoles.csv'

url_datos_resultados = '../Resultados_datos/'
mejores10juegos_consola_empresa = 'mejores10juegos_consola_empresa_'+str(today)+'.csv'
peores10juegos_consola_empresa = 'peores10juegos_consola_empresa_'+str(today)+'.csv'
mejores10juegos = 'mejores10juegos_'+str(today)+'.csv'
peores10juegos = 'peores10juegos_'+str(today)+'.csv'


# Dataframe de datos importados

df_score = pd.read_csv(url_result, sep = ',',  quotechar='"')
df_companies = pd.read_csv(url_consoles, sep = ',')

# Join entre ambos dataframe para obtener 

df = df_score.join(df_companies.set_index('console'), on='console')

# Renombre columna name porque es palabra reservada

df = df.rename(columns={'name':'name_game'})

# Mejores juegos por consola y compañia

def etl_mejores_juegos_consola():

    namegame = list()
    console = list()
    score = list()
    company = list()
    userscore_l = list()
    date_l = list()
    ranking_l = list()
    try:
    # se recorre dataframe df_companies para obtener los valores unicos de consolas e ir filtrando en lam iteracion
        for i in df_companies['console']:
            df_res = df.query(f"""console == '{i}'""")
            df_res = df_res.query('userscore != "tbd"').sort_values('metascore', ascending = False)
            meta_score = list()
            # se obtienen los mayores 10 score y se guarda en un arreglo
            for j in df_res['metascore'].unique():
                if len(meta_score) == 10:
                    break
                else:
                    meta_score.append(j)
            # se utiliza el arreglo de meta_score para obtener el minimo y maximo en el filtro
            df_res = df_res.query(f'metascore >= {min(meta_score)} and metascore <= {max(meta_score)}').sort_values('metascore', ascending = False)
            # se agrega columna rankiando de 1 a 10 los puntajes de cada juego
            df_res["ranking"] = df_res["metascore"].rank(method ='dense', ascending = False)
            # se recorre dataframe y se agregan a listas creadas
            for index, row in df_res.iterrows():
                namegame.append(row.name_game)
                console.append(row.console)
                score.append(row.metascore)
                company.append(row.company)
                userscore_l.append(row.userscore)
                date_l.append(row.date)
                ranking_l.append(row.ranking)
        
        # creacion de dataframe con el total de informacion
        
        df_resultado = pd.DataFrame({'score': score, 'name_game': namegame, 'name_console': console,'userscore': userscore_l, 'date': date_l, 'name_company': company, 'ranking': ranking_l})
    
        # exportar resultado a csv separados por pipe
        df_resultado.to_csv(url_datos_resultados+mejores10juegos_consola_empresa, sep="|", index = False)
    except Exception:
        print("Hubo un error en la funcion etl_mejores_juegos_consola")

# Peores juegos por consola y compañia

def etl_peores_juegos_consola():

    namegame = list()
    console = list()
    score = list()
    company = list()
    userscore_l = list()
    date_l = list()
    ranking_l = list()
    
    try:
    # se recorre dataframe df_companies para obtener los valores unicos de consolas e ir filtrando en lam iteracion
        for i in df_companies['console']:
            df_res = df.query(f"""console == '{i}'""")
            df_res = df_res.query('userscore != "tbd"').sort_values('metascore', ascending = True)
            meta_score = list()
            for j in df_res['metascore'].unique():
                if len(meta_score) == 10:
                    break
                else:
                    meta_score.append(j)
            df_res = df_res.query(f'metascore >= {min(meta_score)} and metascore <= {max(meta_score)}').sort_values('metascore', ascending = False)
            df_res["ranking"] = df_res["metascore"].rank(method ='dense', ascending = False)
            for index, row in df_res.iterrows():
                namegame.append(row.name_game)
                console.append(row.console)
                score.append(row.metascore)
                company.append(row.company)
                userscore_l.append(row.userscore)
                date_l.append(row.date)
                ranking_l.append(row.ranking)
        
        # creacion de dataframe con el total de informacion
        df_resultado = pd.DataFrame({'score': score, 'name_game': namegame, 'name_console': console,'userscore': userscore_l, 'date': date_l, 'name_company': company, 'ranking': ranking_l})
        
        # exportar resultado a csv separados por pipe
        df_resultado.to_csv(url_datos_resultados+peores10juegos_consola_empresa, sep="|", index = False)
    except Exception:
        print("Hubo un error en la funcion etl_peores_juegos_consola")
# Mejores juegos totales     
def etl_mejores_juegos():
    
    try:
        df_res = df.query('userscore != "tbd"').sort_values(['metascore'], ascending = False)
        # se utiliza metodo rank para rankiar a los mejores juegos
        df_res['ranking'] = df_res['metascore'].rank(method='dense', ascending = False)
        df_res = df_res.sort_values('ranking', ascending = True).rename(columns={'console':'name_console', 'metascore':'score', 'company': 'name_company'})
        df_res = df_res.query("ranking <= 10")
        df_res.to_csv(url_datos_resultados+mejores10juegos, sep="|", index = False)
    except Exception:
        print("Hubo un error en la funcion etl_mejores_juegos")
    
# Peores juegos totales   
def etl_peores_juegos():
    
    try:
        df_res = df.query('userscore != "tbd"').sort_values(['metascore','console'], ascending = False)
        df_res['ranking'] = df_res['metascore'].rank(method='dense', ascending = True)
        df_res = df_res.sort_values('ranking', ascending = True).rename(columns={'console':'name_console', 'metascore':'score', 'company': 'name_company'})
        df_res = df_res.query("ranking <= 10")
        df_res.to_csv(url_datos_resultados+peores10juegos, sep="|", index = False)
    except Exception:
        print("Hubo un error en la funcion etl_mejores_juegos")



#Ejecucion de funciones
etl_mejores_juegos_consola()
etl_peores_juegos_consola()
etl_mejores_juegos()
etl_peores_juegos()



