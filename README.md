<<<<<<< HEAD
# Entre Linhas - Fórum de Desabafos Anônimos

Um espaço acolhedor onde usuários podem fazer desabafos anonimamente, comentar e reagir com sensibilidade aos relatos dos outros.

## Sobre o Projeto

Entre Linhas é uma aplicação web desenvolvida com Flask, HTML, CSS e SQLite3 que permite aos usuários:

- Compartilhar desabafos de forma totalmente anônima
- Categorizar os desabafos para melhor organização
- Comentar anonimamente nos desabafos de outros usuários
- Reagir aos desabafos com diferentes tipos de reações (ex: "te entendo", "força!", "abraço virtual")
- Navegar por uma interface acolhedora e responsiva

## Estrutura do Projeto

```
EntreLinhas Project/
├── app.py                  # Configuração principal da aplicação e registro de Blueprints
├── config.py               # Variáveis de configuração (SECRET_KEY, DB_PATH, etc.)
├── database.py             # Funções para conexão e inicialização do banco de dados
├── entrelinhas.db          # Banco de dados SQLite
├── routes/                 # Blueprints para diferentes seções da aplicação
│   ├── __init__.py
│   ├── main.py             # Rotas para a página inicial, sobre, como funciona
│   ├── posts.py            # Rotas para desabafos (feed, envio)
│   ├── comments.py         # Rotas para comentários
│   └── reactions.py        # Rotas para reações
├── templates/              # Arquivos HTML
│   ├── base.html           # Template base para elementos comuns
│   ├── home.html           # Página inicial
│   ├── feed.html           # Página de desabafos
│   ├── about.html          # Página 'Sobre o site'
│   └── how_it_works.html   # Página 'Como funciona'
└── static/
    ├── css/
    │   └── estilos.css     # CSS personalizado
    └── js/
        ├── main.js         # JavaScript geral
        ├── comments.js     # JavaScript para funcionalidades de comentários
        └── reactions.js    # JavaScript para funcionalidades de reações
```

## Funcionalidades

### Página Inicial (Home)
- Introdução ao propósito do site
- Design acolhedor com elementos visuais
- Botão para navegar até os desabafos
- Seções explicativas sobre o funcionamento do site

### Página de Desabafos (Feed)
- Formulário para envio de novos desabafos
- Lista de desabafos existentes
- Sistema de categorização
- Design responsivo e acessível

### Sistema de Comentários
- Comentários anônimos em cada desabafo
- Carregamento assíncrono via JavaScript
- Interface intuitiva para interação

### Sistema de Reações
- Diferentes tipos de reações para expressar apoio
- Contagem de reações para cada desabafo
- Interação em tempo real via JavaScript

### Páginas Adicionais
- Página "Sobre o site" com informações sobre o propósito e valores
- Página "Como funciona" com instruções detalhadas de uso

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite3
- **Frontend**: HTML5, CSS3 (com Tailwind CSS), JavaScript
- **Modularização**: Flask Blueprints

## Como Executar

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install flask
   ```
3. Inicialize o banco de dados:
   ```
   python -c "import database; database.init_db()"
   ```
4. Execute a aplicação:
   ```
   python app.py
   ```
5. Acesse a aplicação em `http://localhost:5000`

## Melhorias Futuras

- Sistema de moderação para conteúdo inadequado
- Opção para filtrar desabafos por categoria
- Paginação para lidar com grande volume de desabafos
- Modo escuro/claro com persistência de preferência
- Estatísticas anônimas sobre temas mais discutidos
=======
# 📝 EntreLinhas — É seu espaço, diga o que sentir.

**EntreLinhas** é um espaço seguro e anônimo onde qualquer pessoa pode compartilhar sentimentos, pensamentos ou desabafos.  
A proposta é simples, mas poderosa: oferecer um lugar onde as palavras possam ser libertas sem julgamento.

> "Às vezes, a gente só precisa ser ouvido — mesmo que por alguém que a gente nunca conheceu."

---

## 💡 Propósito

Muitas vezes não temos com quem conversar, ou simplesmente queremos tirar um peso do peito.  
**EntreLinhas** foi criado para acolher esses momentos.  
Apenas você e o que precisa dizer.

---

## 🔧 Tecnologias usadas

- **Python** com [Flask]
- **HTML5 + CSS3** (modo escuro simples)
- **SQLite** como banco de dados local

---

## 🧩 Funcionalidades

- Enviar desabafos anonimamente
- Escolher uma categoria (ex: estudo, família, sentimentos)
- Feed simples com os desabafos mais recentes
- Banco de dados local com histórico (não visível para o usuário)
- Limite de 500 caracteres para respeitar o espaço de todos

---
>>>>>>> 7220671ada9990da703e916a48699f61aa59dd1f

