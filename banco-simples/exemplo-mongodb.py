from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['teste']
colecao = db['clientes']
cliente1 = {
    'nome': 'Teste',
    'idade': 20,
    'email': 'teste@example.com'
}
colecao.insert_one(cliente1)
clientes = [
    {
        'nome': 'Teste 2',
        'idade': 20,
        'email': 'teste2@example.com'
    },
    {
        'nome': 'Teste 3',
        'idade': 25,
        'email': 'teste3@example.com'
    }
]
colecao.insert_many(clientes)
resultados = colecao.find()
for resultado in resultados:
    print(resultado)

client.close()