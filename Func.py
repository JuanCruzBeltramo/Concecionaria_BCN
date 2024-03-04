def change_col_name(df):
    #ESTA FUNCION CAMBIA EL NOMBRE DE LA COLUMNA DE LA BASE DE DATOS
    #CREAMOS UNA LISTA VACIA PARA DESPUÉS ALMACENAR LOS NOMBRES ACTUALIZADOS DE LAS COLUMNAS
    lista_nombres = []
    for i in range(len(df.columns)):
        # CREAMOS UN BUCLE PARA QUE EL USUARIO INTRODUZCA LOS NUEVOS NOMBRES DE LAS COLUMNAS
        lista_nombres.append(input(f"Introduce el nombre de la columna {i+1}: "))
    #SUSTITUCION DE LOS ANTIGUOS NOMBRES DE LAS COLUMNAS POR LOS ACTUALIZADOS (ANTERIORMENTE GUARDADOS EN LA LISTA)    
    df.columns = lista_nombres
    return df









def val_duplicated(df):
    import pandas as pd 
    if df.duplicated().sum() != 0:
        print(f"Hay un total de {df.duplicated().sum()} valores duplicados")
        if input("Quieres eliminar los valores duplicados? s/n") == 's':
            return df.drop_duplicates(inplace=True)
    else:
        print("No hay valores duplicados")
        return df
    








def ident_cat_num(df): 
    # ESTA FUNCION IDENTIFICA SI LOS DATOS SON DE TIPO NUMERICO O CATEGORICO
    import pandas as pd
    #CREAMOS UNA LISTA PARA DESPUÉS ALMACENAR LOS NOMBRES DE LAS COLUMNAS QUE SEAN NUMERICAS
    list_numericas = [] 
    #CREAMOS UNA LISTA PARA DESPUÉS ALMACENAR LOS NOMBRES DE LAS COLUMNAS QUE SEAN CATEGORICAS
    list_categoricas = []
    #RECORREMOS LAS COLUMNAS DE LA BASE DE DATOS
    for i in df.columns: 
        #IDENTIFICAMOS SI LOS DATOS QUE CONTIENE LA COLUMNA SON NUMERICOS
        if pd.api.types.is_numeric_dtype(df[i])== True:
            #ALMACENAMOS LOS NOMBRES DE LAS COLUMNAS QUE SEAN NUM
            list_numericas.append(i)
        else:
            #SINO LOS ALMACENAMOS LOS NOMBRES DE LAS COLUMNAS QUE SEAN CATEGORICAS
            list_categoricas.append(i)
    return list_numericas,list_categoricas







def val_nulos(df):
    # ESTA FUNCION IDENTIFICA LOS VALORES NULOS Y PREGUNTA AL USUARIO SI QUIERES ELIMINARLOS O NO
    #SI HAY VALORES NULOS MUESTRA EL TOTAL
    if df.isnull().sum() != 0:
        print(f"Hay {df.isnull().sum()} valores nulos")
        if input("Quieres eliminar los valores nulos? s/n") =='s':
            df.dropna(inplace=True)
        else:
            return df
    else:
        print("No hay valores nulos")
        return df
  
def OrdinalEncoder(df,col,lista_columnas):
    import sklearn as skl
    from sklearn.preprocessing import OrdinalEncoder
    encoder = OrdinalEncoder(categories=[[lista_columnas]])
    encoder.fit(df[col])
    df[col] = encoder.transform(df[col])
    return df


    

def outliers(d,v):
    import numpy as np
    q3=np.quantile(d[v],0.75)
    q1=np.quantile(d[v],0.25)
    ric=q3-q1
    df_outliers=d.loc[(d[v]>=q3+1.5*ric) | (d[v]<=q1-1.5*ric), : ]
    df_limpio= d.loc[(d[v]<q3+1.5*ric) & (d[v]>q1-1.5*ric), : ]
    return df_outliers,df_limpio

num = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
for i in num:
    a,b=outliers(df,i)
    df = b