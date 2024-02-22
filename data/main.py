import pandas as pd 
df=pd.read_csv('data/reseau_en_arbre.csv')
#print(df.head())

df_touche=df.query('infra_type == "a_remplacer"')
print(df_touche.head())

infrac_subdfs= df_touche.groupby(by="infra_id")
for infra_id,infrac_subdf in infrac_subdfs:
    print(infra_id)
    print(infrac_subdf)
    print("_"*30)