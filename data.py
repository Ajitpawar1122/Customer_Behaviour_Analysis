

import pandas as pd
from pygame.midi import frequency_to_midi
from sqlalchemy import create_engine
from sqlalchemy.testing.plugin.plugin_base import engines

df=pd.read_csv('customer_shopping_behavior.csv')

print(df.head())
print()
print(df.info())
print()
print(df.describe(include='all'))
print()
print(df.isnull().sum())
print()
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
print()
#create a column age_group
labels=['young adult','adult','middle-aged','senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(9))
print()

#create columns purchase_frequency_days
frequency_mapping={
    'fortnightly':14,
    'weekly':7,
    'monthly':30,
    'quarterly':90,
    'bi_weekly':14,
    'annually':365,   # spelling fix keli - double 'n'
    'annualy':365,    # tujhi junhi pan thevli
    'every 3 months':90,
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].str.lower().map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(9))
print()
print(df[['discount_applied','promo_code_used']].head(9))
df=df.drop('promo_code_used',axis=1)
print(df.columns)
import pandas as pd
from sqlalchemy import create_engine

# 1. CSV read kar
df = pd.read_csv("D:/Data Analytics projects/Portfolio/customer_shopping_behavior.csv")
print("CSV loaded:", df.shape)

# 2. DB che details define kar
user = "postgres"
password = "8637"      # Tujha password
host = "localhost"
port = "5432"
database = "customer_behaviour"  # pgAdmin madhe ha database banavla ahe na?
table_name = "shopping_data"

# 3. Engine banav
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# 4. Data DB madhe tak
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f"Data successfully loaded into '{table_name}' in database '{database}'.")
