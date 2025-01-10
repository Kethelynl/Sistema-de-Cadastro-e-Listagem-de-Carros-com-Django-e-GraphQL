
# Sistema de Cadastro e Listagem de Carros com Django e GraphQL

Este é um projeto de um sistema simples para cadastro e listagem de carros utilizando Django e GraphQL. O sistema permite registrar carros, com campos como modelo, placa, cor e tipo de serviço. Além disso, é possível consultar todos os carros cadastrados.

## Tecnologias Usadas

-  **Django**: Framework web para Python.
- **Graphene-Django**:  Biblioteca para integrar o GraphQL com o Django.
- **SQLite**: (por padrão no Django): Banco de dados utilizado para armazenar os dados.

## Funcionalidades

- **Cadastro de Carros**: Permite o cadastro de carros, com as informações:
- **Modelo**
- **Placa**
- **cor**
- **Tipo de Serviço**
- **Listagem de Carros**: Permite consultar todos os carros cadastrados.
- **Validação de Placa Única: **: A placa de veículo é única, ou seja, dois carros não podem ter a mesma placa.


## Instalação
### Requisitos
Antes de começar, certifique-se de ter o Python instalado na sua máquina.

Python 3.8 ou superior
Pip (gerenciador de pacotes do Python)

### Passos para Instalação
Clone o repositório:
```bash
  git clone https://github.com/seu-usuario/nome-do-repositorio.  git
  cd nome-do-repositorio
```

### Crie um ambiente virtual (recomendado):
```bash
python -m venv env
```
Ative o ambiente virtual:

No Windows:

```bash
env\Scripts\activate
```

No Linux/macOS:

```bash
source env/bin/activate
```
### Instale as dependências
```bash
pip install -r requirements.txt
```
### Execute as migrações
```bash
python manage.py migrate
```

### Inicie o servidor
```bash
python manage.py runserver
```
A API estará disponível em:
http://127.0.0.1:8000/api/

## Como Usar
### API GraphQL
Com a aplicação rodando, você pode acessar o endpoint GraphQL em:
- URL do GraphQL: http://127.0.0.1:8000/graphql/

Na interface do GraphQL, você pode realizar as seguintes operações:

#### Cadastrar um carro (Mutation)
```bash
mutation {
  createCar(model: "Fusca", licensePlate: "ABC-1234", color: "Blue", serviceType: "wash") {
    car {
      model
      licensePlate
      color
      serviceType
    }
  }
}
```

#### Listar todos os carros (Query)
```bash
query {
  allCars {
    model
    licensePlate
    color
    serviceType
  }
}
```

### Exemplo de resposta para a consulta allCars:
```bash
{
  "data": {
    "allCars": [
      {
        "model": "Fusca",
        "licensePlate": "ABC-1234",
        "color": "Blue",
        "serviceType": "wash"
      },
      {
        "model": "Gol",
        "licensePlate": "XYZ-5678",
        "color": "Red",
        "serviceType": "polish"
      }
    ]
  }
}
```
## Estrutura do Projeto
- **models.py**: Contém o modelo Car, com os campos do carro e a escolha de tipo de serviço.
- **schema.py**: Define a Query para listar todos os carros e a Mutation para criar um novo carro.
- **urls.py**: Configurações das URLs para o Django.
- **settings.py**: Configurações principais do Django, incluindo banco de dados e integração com GraphQL.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções, fique à vontade para criar um pull request.

#### Como Contribuir
- 1. **Faça o fork deste repositório.**
- 2. **Crie uma branch com a sua feature ou correção.**
- 3. **Faça commit das suas alterações.**
- 4. **Abra um pull request.**
