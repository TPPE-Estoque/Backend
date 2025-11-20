# ⚙️ Backend - Gerenciador de Estoque

![Status](https://img.shields.io/badge/status-em--desenvolvimento-yellow)

Este repositório contém o código-fonte da API (Backend) para o projeto de **Gerenciamento de Estoque**. A aplicação é desenvolvida com Django e Django REST Framework, e é totalmente containerizada com Docker para garantir um ambiente de desenvolvimento consistente e de fácil configuração.

## 🛠️ Tecnologias Utilizadas

-   **[Python](https://www.python.org/)**: Linguagem principal da aplicação.
-   **[Django](https://www.djangoproject.com/)**: Framework web para o desenvolvimento da API.
-   **[Django REST Framework](https://www.django-rest-framework.org/)**: Toolkit para a construção de APIs Web.
-   **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados relacional.
-   **[Docker](https://www.docker.com/)** & **[Docker Compose](https://docs.docker.com/compose/)**: Para containerização e orquestração dos serviços.
-   **[Gunicorn](https://gunicorn.org/)**: Servidor WSGI para produção.

## 🔗 Repositórios do Projeto

Este projeto é dividido em múltiplos repositórios. Acesse os outros componentes através dos links abaixo:

-   **[📄 Documentação](https://github.com/EcoStock-organization/ecostock-docs)**
-   **[🖥️ Frontend](https://github.com/EcoStock-organization/ecostock-frontend)**
-   **[🔑 Serviço de Autenticação](https://github.com/EcoStock-organization/Auth)**

## 🚀 Como Rodar o Projeto

Graças ao Docker, você não precisa instalar Python, Django ou PostgreSQL na sua máquina. Apenas o Docker é necessário.

### Pré-requisitos

-   **[Docker](https://docs.docker.com/get-docker/)**
-   **[Docker Compose](https://docs.docker.com/compose/install/)**

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/EcoStock-organization/ecostock-backend.git
    cd Backend
    ```

2.  **Construa e inicie os contêineres:**
    Este comando irá baixar a imagem do Postgres e construir a imagem da sua aplicação Django.
    ```bash
    docker-compose up --build -d
    ```

3.  **Execute as migrações do banco de dados:**
    Com os contêineres rodando, execute o comando `migrate` para criar as tabelas no banco de dados.
    ```bash
    docker-compose exec backend python src/manage.py migrate
    ```

Pronto! A API estará rodando e acessível em **[http://localhost:8000](http://localhost:8000)**.

