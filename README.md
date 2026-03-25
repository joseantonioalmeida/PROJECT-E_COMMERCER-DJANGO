#  E-Commerce Django — Sistema de Vendas

Este é um projeto de E-commerce profissional desenvolvido com o framework Django 6. Ele oferece uma plataforma robusta para listagem de produtos, gerenciamento de variações (tamanhos, cores), sistema de carrinho de compras e área do cliente.

Além da aplicação, o projeto foi arquitetado para rodar em ambientes de produção utilizando Docker, garantindo que toda a pilha de serviços (Python/Django, PostgreSQL, Gunicorn e Nginx) funcione de forma orquestrada.

---

#  Funcionalidades

## 🔐 Autenticação e Usuários

  ✔ Cadastro de Clientes: Formulários validados com Crispy Forms e Bootstrap 4.
  
  ✔ Login/Logout Seguro: Utiliza o sistema de autenticação nativo do Django com proteção de sessão.
  
  ✔ Área do Cliente (Perfil): Espaço para o usuário atualizar seus dados cadastrais, endereço e CPF.


## 📦 Gestão de Produtos

  ✔ Catálogo Dinâmico: Listagem de produtos com busca integrada.
  
  ✔ Variações de Produto: Suporte a diferentes atributos (ex: Tamanho P, M, G) com preços distintos para a mesma base de produto.
  
  ✔ Otimização de Mídia: Redimensionamento automático de imagens no upload para garantir performance (Pillow).
  
  ✔ SEO & Slugs: URLs amigáveis geradas automaticamente para melhor indexação.


## 🛒 Experiência de Compra

  ✔ Sistema de Carrinho: Lógica baseada em sessões que permite adicionar, remover e alterar quantidades de itens em tempo real.
  
  ✔ Gestão de Pedidos: Após o checkout, o sistema gera um registro de pedido vinculado ao perfil do usuário, mantendo o histórico de compras.

---

# 🛠 Tecnologias e Infraestrutura

## Desenvolvimento & Produção:

  *Linguagem: Python 3.13.

  *Framework Web: Django 6.0
  
  *Banco de Dados: PostgreSQL (Produção)
  
  *Processamento de Imagem: Pillow (LANCZOS para alta qualidade)
  
  *Front-end: HTML5, CSS3, JavaScript, Bootstrap 4 e Font Awesome.
  
  *Infraestrutura: Docker & Docker Compose.
  
  *Middleware de Formulários: Django Crispy Forms.

## Deploy & DevOps:
  *SO: Windows 11 com WSL2 (Ubuntu 22.04).
  
  *Orquestração: Docker & Docker Compose.
  
  *Porta de Saída: 80 (HTTP Padrão).
  
  *Web Server: Nginx (Proxy Reverso e entrega de arquivos estáticos/mídia no Linux).
  
  *App Server: Gunicorn (WSGI HTTP Server).
  
  *Controle de Versão: Git (Fluxo de deploy via Git Push do Windows para o repositório Bare no WSL2).

---

## 🏗 Arquitetura do Deploy (WSL2 + Docker)

O servidor foi estruturado para ser acessível diretamente pela rede:

1. Ponte de Rede: O Windows redireciona o tráfego para o IP interno do WSL2 (172.26.126.18)

2. Docker Compose: Orquestra dois containers principais:

      2.1 ecommerceapp: Roda a lógica do Python em um ambiente isolado (usuário duser).

      2.2 psql: Banco de dados PostgreSQL com persistência em volume.

3. Nginx (Host WSL2): Escuta na porta 80 do Linux, serve diretamente os arquivos das pastas /data/web/static e /data/web/media. E repassando requisições para o Gunicorn.

4. Gunicorn: Gerencia os processos do Django através de um Unix Socket (/run/ecommerce.socket), conectando-se ao PostgreSQL para persistência de dados.

---

## 💡 Estrutura do Projeto

📦 PROJECT-E_COMMERCER-DJANGO

┣ 📂 ecommerceapp (Core do projeto e configurações da Loja) 

┣ 📂 produto (App de gestão de produtos e variações)

┣ 📂 pedido (App para processamento de compras e checkout)

┣ 📂 perfil (App para gestão de contas de usuários)

┣ 📂 scripts (Automação de inicialização do container) 

┣ 📂 static (CSS, JS e Assets globais)

┣ 📜 Dockerfile (Configuração da imagem Python 3.13) 

┗ 📜 docker-compose.yml (Orquestração dos serviços)


---
## 🚀 Guia de Uso: Do Setup ao Primeiro Pedido

Este guia explica como configurar o ambiente e utilizar as principais funcionalidades da plataforma.

### 1. Requisitos Prévios.
    Antes de começar, certifique-se de ter instalado:
    
      1.2 Docker e Docker Compose;
      
      1.3 Git.
      
### 2. Instalação e Inicialização (Setup).
Siga os comandos no seu terminal para subir o ecossistema:

    2.1 Clonagem e Pastas:
      2.1.1 git clone https://github.com/joseantonioalmeida/PROJECT-E_COMMERCER-DJANGO.git
      2.1.2 cd PROJECT-E_COMMERCER-DJANGO
      
    2.2 Variáveis de Ambiente:
      2.2.1 Certifique-se de que o arquivo .env em dotenv_files/ contenha as credenciais do Postgres e a SECRET_KEY.

    2.3 Subir Containers:
      2.3.1 docker-compose up --build

    2.4 Migrações e Superusuário:
      2.4.1 docker exec -it ecommerceapp python manage.py migrate
      2.4.2 docker exec -it ecommerceapp python manage.py createsuperuser

### 3. Fluxo de Uso do Usuário (Cliente).

#### A. Navegação e Busca
      Ao acessar http://localhost:8000, o usuário é recebido pela vitrine de produtos.
      Utilize a barra de busca no topo para buscar/filtrar produtos por nome ou descrição. O sistema utiliza filtros icontains do Django para buscas parciais.

#### B. Gestão do Carrinho
      Ao clicar em um produto, escolha a Variação (ex: Tamanho ou Cor).
      Clique em "Adicionar ao Carrinho". O sistema utiliza sessões do navegador, permitindo que você continue comprando sem perder os itens, mesmo sem estar logado.
      No ícone do carrinho, você pode aumentar ou diminuir a quantidade de cada item.

#### C. Cadastro e Login
      Para finalizar a compra, o sistema exigirá autenticação.
      Se for um novo usuário, preencha o formulário de cadastro (Perfil). O Django validará o CPF e o endereço automaticamente.

#### D. Finalização de Pedido
      No checkout, revise seus itens. Ao confirmar, o carrinho é esvaziado e um registro permanente é criado na tabela de Pedidos.
      Acesse "Meus Pedidos" para visualizar o histórico de compras e o status de cada transação.


### 4. Fluxo do Administrador (Lojista)

O administrador tem controle total sobre o catálogo através do painel: http://localhost:8000/admin.

      Cadastrar Produtos: Ao fazer o upload de uma imagem, o sistema ativa o processamento via Pillow, redimensionando fotos pesadas para o padrão de 800px.
      Gerenciar Variações: Para cada produto, o lojista deve adicionar variações. Se um produto for "Camisa", as variações podem ser "M" e "G", cada uma com seu próprio estoque.
      Controle de Estoque: O sistema impede que um usuário adicione ao carrinho mais itens do que o disponível no campo estoque da Variação.

---

## 💬 O que eu Aprendi com esse Projeto

  *1. Domínio da Arquitetura MVT e Modularidade
        Aprendi a importância de dividir uma aplicação complexa em apps independentes (produto, pedido, perfil). 
        Isso facilita a manutenção e permite que cada parte do sistema cresça sem afetar as outras. 
        Entendi como o Django orquestra o fluxo de dados entre o Banco de Dados (Model), a lógica de negócio (View) e a interface do usuário (Template).

  *2. DevOps e Containerização Profissional
        Minha maior evolução foi tirar a aplicação do "local" e colocá-la no Docker.
        Aprendi a criar imagens customizadas com o Dockerfile.
        Entendi como usar o docker-compose para fazer o Django "conversar" com o PostgreSQL em redes isoladas.
        Aprendi a gerenciar volumes, garantindo que as imagens dos produtos e os dados dos clientes não sumam quando o container é reiniciado.
  

  *3. Engenharia de Dados com PostgreSQL
        Saí do básico de bancos de dados para lidar com situações reais de produção:
        Migrações Complexas: Aprendi a resolver erros de integridade quando adicionamos campos novos em tabelas que já têm dados.
        Relacionamentos: Implementei relações de ForeignKey para criar o sistema de variações de produtos (Pai e Filho).
        Performance: Aprendi a usar o Pillow para processar e redimensionar imagens no backend, garantindo que o site carregue rápido para o usuário final.

  *4. Lógica de Negócio e Gestão de Estado
        Desenvolver o Carrinho de Compras me ensinou a trabalhar com Sessões (Sessions). 
        Compreendi como manter dados temporários do usuário enquanto ele navega pelo site, transformando esses dados em um registro permanente (Pedido) apenas no momento final do checkout.
  
  *5. Infraestrutura Linux e DevOps (WSL2):
  
        Saí do básico e passei a gerenciar um servidor Linux real dentro do meu ambiente Windows via WSL2. 
        Aprendi a configurar o Nginx como um proxy reverso profissional, lidando com diretivas críticas como o client_max_body_size para permitir o upload de arquivos grandes. 
        Também dominei o sistema de permissões do Linux (chmod/chown), garantindo que o servidor web e o Django possam ler e gravar arquivos de mídia com segurança.

  💡 Conclusão
      Este e-commerce não é apenas um site; é um ecossistema completo. 
      Aprendi que ser um desenvolvedor Full Stack é saber equilibrar uma interface amigável (Frontend), uma lógica segura (Backend) e uma infraestrutura sólida (DevOps).

---

##  Como Rodar o Projeto Localmente (via Docker)

1. Clone o repositório:
git clone https://github.com/joseantonioalmeida/PROJECT-E_COMMERCER-DJANGO.git

2. Acesse a pasta:
cd PROJECT-E_COMMERCER-DJANGO

3. Configure o arquivo .env:
Crie o arquivo em dotenv_files/.env com suas credenciais.

4. Suba o Ambiente:
docker-compose up --build

5. Crie um ambiente virtual:
python -m venv venv

6. Ative o ambiente:
Windows:
  venv\Scripts\activate

macOS / Linux:
  source venv/bin/activate

7. Crie um super usuário (opcional):
python manage.py createsuperuser

8.Acesse o site:
👉 http://localhost:8000 ou http://172.26.126.18 (se o Nginx estiver ativo).

---
## 🌍 Detalhes do Deploy (Modo Produção)
Para quem deseja replicar o deploy em ambiente Linux:

   1.Repositório Bare: Criado no WSL2 para receber o código via git push direto do Windows.
   2. Nginx no WSL2: Configurado para apontar para o container Docker.
   3. Ajuste de Permissões: Uso de chown -R duser:duser nos volumes para garantir que o Django consiga gravar as imagens enviadas.
   
---
