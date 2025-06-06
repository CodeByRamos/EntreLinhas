## Plano de Melhorias e Novas Funcionalidades para o Fórum de Desabafos Anônimos

Este documento detalha o plano para aprimorar o projeto "Entre Linhas", um fórum de desabafos anônimos desenvolvido com Flask, HTML, CSS e SQLite3. O objetivo é criar um espaço mais acolhedor, funcional e visualmente atraente, incorporando as funcionalidades solicitadas pelo usuário.

### 1. Análise da Estrutura Atual

O projeto atual consiste em:

*   **`app.py`**: O arquivo principal da aplicação Flask, contendo a lógica de roteamento, manipulação de banco de dados e renderização de templates.
*   **`init_db.py`**: Um script separado para inicializar o banco de dados SQLite (`entrelinhas.db`).
*   **`entrelinhas.db`**: O banco de dados SQLite, que atualmente possui uma tabela `posts` para armazenar os desabafos.
*   **`templates/`**: Contém os arquivos HTML (`home.HTML` e `feed.html`).
*   **`static/css/estilos.css`**: Arquivo CSS para estilos personalizados.
*   **`static/`**: Diretório para arquivos estáticos.

A tabela `posts` no banco de dados, conforme observado em `init_db.py`, possui as seguintes colunas:

*   `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
*   `mensagem` (TEXT NOT NULL)
*   `data_postagem` (TEXT NOT NULL)
*   `categoria` (TEXT)
*   `reacoes` (INTEGER DEFAULT 0)
*   `visivel` (INTEGER DEFAULT 1)

Foi notada uma inconsistência entre a definição da tabela `posts` em `app.py` e `init_db.py`. A versão em `init_db.py` é mais completa, incluindo a coluna `reacoes`. A versão em `init_db.py` será considerada a fonte da verdade e `app.py` será atualizado para refletir essa estrutura.

O arquivo `home.HTML` atualmente redireciona imediatamente para `/feed`, o que será alterado para criar uma página inicial adequada. O `feed.html` já utiliza Tailwind CSS, o que será aproveitado para as melhorias visuais.

### 2. Melhorias e Novas Funcionalidades

As seguintes melhorias e funcionalidades serão implementadas:

#### 2.1. Página Inicial (Home)

*   **Propósito**: Criar uma página de boas-vindas que introduza o conceito do fórum de desabafos anônimos.
*   **Conteúdo**: Texto acolhedor, explicação breve do propósito do site, e um botão claro para navegar para a página de desabafos (`/feed`).
*   **Design**: Utilizar Tailwind CSS para um design moderno, limpo e responsivo, transmitindo uma sensação de acolhimento e segurança.
*   **Arquivo**: `templates/home.html` (será reescrito).

#### 2.2. Melhoria da Página de Desabafos (Feed)

*   **Visual**: Aprimorar o design existente utilizando mais recursos do Tailwind CSS para melhorar a legibilidade, espaçamento e a estética geral dos desabafos e do formulário de envio.
*   **Funcionalidade**: Integrar os sistemas de comentários e reações de forma intuitiva. Considerar a adição de um mecanismo de carregamento de desabafos (e.g., paginação ou carregamento infinito) se o volume de dados justificar.
*   **Arquivo**: `templates/feed.html` (será modificado).

#### 2.3. Sistema de Comentários Anônimos

*   **Funcionalidade**: Permitir que os usuários comentem anonimamente em cada desabafo.
*   **Estrutura do Banco de Dados**: Será criada uma nova tabela `comments`.
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
    *   `post_id` (INTEGER, FOREIGN KEY para `posts.id`)
    *   `comment_text` (TEXT NOT NULL)
    *   `data_comentario` (TEXT NOT NULL)
    *   `visivel` (INTEGER DEFAULT 1)
*   **Backend**: Rota Flask para receber e armazenar comentários. Função para recuperar comentários associados a um desabafo específico.
*   **Frontend**: Formulário de comentário abaixo de cada desabafo. Exibição dos comentários de forma organizada. Utilização de JavaScript (AJAX) para submissão de comentários sem recarregar a página.

#### 2.4. Sistema de Reações aos Desabafos

*   **Funcionalidade**: Permitir que os usuários reajam aos desabafos com opções predefinidas (ex: “te entendo”, “força!”, “abraço virtual”).
*   **Estrutura do Banco de Dados**: Será criada uma nova tabela `reactions`.
    *   `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
    *   `post_id` (INTEGER, FOREIGN KEY para `posts.id`)
    *   `reaction_type` (TEXT NOT NULL, e.g., 'te_entendo', 'forca', 'abraco_virtual')
    *   `data_reacao` (TEXT NOT NULL)
*   **Backend**: Rota Flask para registrar reações. Função para atualizar e recuperar a contagem de cada tipo de reação para um desabafo.
*   **Frontend**: Botões de reação visíveis em cada desabafo. Exibição da contagem de cada reação. Utilização de JavaScript (AJAX) para registrar reações sem recarregar a página.

#### 2.5. Páginas Adicionais

*   **Propósito**: Fornecer informações adicionais sobre o site e seu funcionamento.
*   **Páginas**: `Sobre o site` (`templates/about.html`) e `Como funciona` (`templates/how_it_works.html`).
*   **Conteúdo**: Textos informativos e explicativos.
*   **Design**: Seguir o mesmo padrão visual das demais páginas, utilizando Tailwind CSS.

### 3. Estrutura do Código (Modularização com Blueprints)

Para garantir um código limpo, organizado e escalável, a aplicação será reestruturada utilizando Flask Blueprints. A nova estrutura de diretórios será:

```
EntreLinhas Project/
├── app.py                  # Configuração principal da aplicação e registro de Blueprints
├── config.py               # Variáveis de configuração (e.g., SECRET_KEY, DB_PATH)
├── database.py             # Funções centralizadas para conexão e inicialização do banco de dados
├── init_db.py              # Script para inicialização do banco de dados (mantido para referência)
├── entrelinhas.db          # Banco de dados SQLite
├── routes/                 # Contém os Blueprints para diferentes seções da aplicação
│   ├── __init__.py
│   ├── main.py             # Rotas para a página inicial, sobre, como funciona
│   ├── posts.py            # Rotas para desabafos (feed, envio)
│   ├── comments.py         # Rotas para comentários
│   └── reactions.py        # Rotas para reações
├── templates/              # Arquivos HTML
│   ├── base.html           # Template base para elementos comuns (cabeçalho, rodapé, navegação)
│   ├── home.html           # Nova página inicial
│   ├── feed.html           # Página de desabafos atualizada
│   ├── about.html          # Página 'Sobre o site'
│   └── how_it_works.html   # Página 'Como funciona'
└── static/
    ├── css/
    │   └── estilos.css     # CSS personalizado (além do Tailwind)
    └── js/
        ├── main.js         # JavaScript geral
        ├── comments.js     # JavaScript para funcionalidades de comentários
        └── reactions.js    # JavaScript para funcionalidades de reações
```

### 4. Tecnologias e Ferramentas

*   **Backend**: Flask (Python)
*   **Banco de Dados**: SQLite3
*   **Frontend**: HTML5, CSS3 (com Tailwind CSS), JavaScript
*   **Modularização**: Flask Blueprints

### 5. Próximos Passos

1.  **Atualizar o esquema do banco de dados**: Modificar `init_db.py` e `app.py` para incluir as novas tabelas `comments` e `reactions`, e ajustar a tabela `posts` se necessário.
2.  **Reestruturar o projeto**: Criar os diretórios e arquivos conforme a nova estrutura de Blueprints.
3.  **Implementar a página inicial**: Desenvolver o novo `home.html` e a rota correspondente.
4.  **Refatorar a página de desabafos**: Adaptar `feed.html` para a nova estrutura e preparar para a integração de comentários e reações.
5.  **Desenvolver o sistema de comentários**: Implementar backend e frontend.
6.  **Desenvolver o sistema de reações**: Implementar backend e frontend.
7.  **Criar páginas adicionais**: Desenvolver `about.html` e `how_it_works.html`.
8.  **Testes**: Realizar testes completos de todas as funcionalidades.
9.  **Documentação**: Garantir que o código esteja bem comentado e que a documentação seja clara.


