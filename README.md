
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

- ## Melhorias Futuras

- Sistema de moderação para conteúdo inadequado
- Opção para filtrar desabafos por categoria
- Paginação para lidar com grande volume de desabafos
- Modo escuro/claro com persistência de preferência
- Estatísticas anônimas sobre temas mais discutidos

---
>>>>>>> 7220671ada9990da703e916a48699f61aa59dd1f

