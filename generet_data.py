 
import pandas as pd
import faker

numero_de_pessoas = 20000

fake = faker.Faker()
df = pd.DataFrame(
    data=[
        [fake.name(), fake.random_int(min=1, max=20), fake.boolean()]
        for _ in range(numero_de_pessoas)
    ],
    columns=["name", "zone", "infected"],
)

df.to_csv("fake_data.csv")

import random

# Criar uma lista de todos os nomes
names = df['name'].tolist()

# Criar um conjunto para armazenar pares de amigos já criados
friend_pairs = set()

# Criar uma lista para armazenar os pares de amigos
friend_list = []

# Para cada nome na lista de nomes
for name in names:
    # Sortear um número de amigos que a pessoa tem
    num_friends = random.randint(1, 20)
    
    # Para cada amigo
    for _ in range(num_friends):
        # Sortear um amigo da lista de nomes
        friend = random.choice(names)
        
        # Certificar-se de que a pessoa não é amiga de si mesma e que o par de amigos ainda não foi criado
        while friend == name or (name, friend) in friend_pairs or (friend, name) in friend_pairs:
            friend = random.choice(names)
        
        # Adicionar o par de amigos ao conjunto de pares de amigos
        friend_pairs.add((name, friend))
        
        # Adicionar o par de amigos à lista de pares de amigos
        friend_list.append([name, friend])

# Criar um DataFrame a partir da lista de pares de amigos
df_friends = pd.DataFrame(friend_list, columns=['pessoa1', 'pessoa2'])

# Salvar o DataFrame como um arquivo CSV
df_friends.to_csv('friendship_data.csv', index=False)
