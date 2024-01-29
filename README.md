# Community-V3

Português | [English](README.MD)

[![Repository Views](https://komarev.com/ghpvc/?username=kensdycommunityv3&label=Views&color=brightgreen)](https://github.com/kensdy/Community-V3)

## Como Usar

1. **Pré-requisitos:**
   - Certifique-se de ter o Python instalado em sua máquina.

2. **Clonando o Repositório:**
   - Execute o seguinte comando para clonar o repositório:
     ```bash
     git clone https://github.com/kensdy/Community-V3
     ```
3. **Executando o Aplicativo:**
   - Navegue para o diretório recém-clonado com `cd Community`.
   - Instale as dependências usando `pip install -r requirements.txt`.
   - Execute `python main.py` para iniciar o servidor local.
   - Acesse `http://127.0.0.1:5000` em seu navegador para interagir com o fórum.

**Conhecendo as Funcionalidades**

O Community apresenta diversas funcionalidades que visam proporcionar uma experiência robusta e amigável para os usuários:

### 1. Página Inicial (Home)

A Página Inicial exibe uma lista de todos os posts já criados no site, organizados com os mais recentes no topo da lista. Esta é a porta de entrada para a comunidade, proporcionando uma visão abrangente das discussões em andamento.
![Home](home.png)

### 2. Página de Criação de Posts

Na Página de Criação de Posts, os usuários podem contribuir para a comunidade compartilhando suas ideias, experiências ou perguntas. Basta fornecer um título, um apelido (nick), e o conteúdo desejado. A formatação utilizando markdown é suportada para enriquecer o conteúdo.
![Criar Post](criarpost.png)

### 3. Página de Leitura de Posts

A Página de Leitura de Posts permite que os usuários acessem postagens específicas para leitura mais detalhada. Além disso, nesta página, é possível interagir com o conteúdo, deixando comentários nas postagens existentes. Isso promove uma experiência dinâmica de discussão, permitindo que a comunidade se envolva ativamente nos tópicos apresentados.

### 4. Sistema de Posts e Comentários

O sistema de posts e comentários é a espinha dorsal do Community, proporcionando uma plataforma para compartilhar ideias e expressar opiniões. Os usuários podem interagir de maneira fácil e intuitiva, estimulando discussões dinâmicas.
![Post e Comentários](post.png)

### 5. Sem Necessidade de Login

Não é necessário realizar login para interagir com o Community. Essa abordagem simplifica o acesso, permitindo que os usuários participem rapidamente das discussões sem a necessidade de criar uma conta.

### 6. Sistema de Banco de Dados em Arquivo JSON

O Community utiliza um sistema de armazenamento em arquivo JSON para os posts e comentários. Essa escolha oferece simplicidade e facilidade de personalização, eliminando a necessidade de um banco de dados mais complexo.

### 7. Sistema de Logs de Acessos ao Site

O arquivo `audit_log.txt` registra todas as interações com o site, incluindo informações essenciais, como endereço IP e horário de acesso. Esse sistema de logs possibilita o rastreamento e a análise do tráfego no site.

### 8. Sistema de Ban por IP

O Community apresenta uma funcionalidade de banimento por IP. No arquivo `blocked_ips.json`, é possível bloquear o acesso de IPs específicos, redirecionando-os para uma página de bloqueio (`blocked.html`) ao tentar acessar o site.


### Bloqueio de Acesso por IP

Para restringir o acesso de determinados IPs ao site, você pode utilizar o arquivo `blocked_ips.json`. Siga os passos abaixo:

1. **Localize o Arquivo `blocked_ips.json`:**
   - Abra o arquivo `blocked_ips.json` no diretório do projeto.

2. **Adicionando IPs Bloqueados:**
   - Insira os IPs que você deseja bloquear no formato JSON. Por exemplo:
     ```json
     ["248.161.103.175", "142.57.70.192"]
     ```
     Isso bloqueará o acesso dos IPs listados.
     ![blocked_ips.json](bip.png)

3. **Redirecionamento para a Página de Bloqueio:**
   - Quando um usuário com IP bloqueado tenta acessar o site, será automaticamente redirecionado para a página de bloqueio (`blocked.html`).
    ![Página de Bloqueio](blocked.png)

> **Nota:** Certifique-se de ajustar a página `blocked.html` conforme necessário para fornecer informações adequadas aos usuários bloqueados.

Isso garante um controle eficiente sobre o acesso ao site, permitindo que você restrinja específicos IPs e ofereça uma experiência de redirecionamento personalizada para aqueles que estão bloqueados.

### Registro de Auditoria

No arquivo `audit_log.txt`, você pode encontrar um registro detalhado de todos os acessos ao site, incluindo informações cruciais como o endereço IP e o horário de acesso. Esta funcionalidade proporciona uma visão abrangente das interações com o seu site, permitindo monitorar e analisar o tráfego com precisão.

#### Como Utilizar

1. **Localização do Arquivo:**
   - Abra o arquivo `audit_log.txt` no diretório do projeto.

     ![Arquivo de Logs](log.png)

2. **Conteúdo do Registro:**
   - Cada linha do arquivo representa uma entrada de registro, exibindo o IP do usuário e o horário de acesso.

     ```plaintext
     Acesso do IP: xxx.xxx.xxx.xxx - [Data e Hora]
     ```

3. **Análise de Acessos:**
   - Utilize esse registro para rastrear padrões de acesso, identificar atividades suspeitas ou simplesmente monitorar a frequência de visitas ao seu site.

### Gerenciamento de Dados

No arquivo `data.json`, a base de dados de posts é armazenada, oferecendo funcionalidades de gerenciamento essenciais. Além de conter informações sobre as postagens, este arquivo proporciona recursos adicionais:

#### 1. **Apagar Postagens:**
   - Através do arquivo `data.json`, é possível excluir postagens conforme necessário. Basta localizar a entrada correspondente e removê-la do arquivo para realizar a exclusão.

     ![data.json](data.png)

#### 2. **Informações Adicionais:**
   - O arquivo também inclui detalhes adicionais sobre as postagens, como o IP do usuário que as criou. Isso fornece uma visão mais abrangente das atividades dos usuários.

   ```json
{
  "posts": [
    {
      "id": 1,
      "title": "Título da Postagem",
      "content": "Conteúdo da Postagem",
      "author": "Nome do Autor",
      "timestamp": "Data e hora",
      "comments": [
        {
          "author": "Nome do Autor",
          "content": "Conteúdo do Comentário",
          "ip_address": "248.161.103.175"
        }
      ],
      "ip_address": "142.57.70.192"
    }
  ]
}
   ```

#### 3. **Rastreamento de IP:**
   - O campo `user_ip` em cada entrada permite rastrear o IP do autor da postagem, oferecendo uma camada adicional de informação sobre a origem das interações no seu site.

Utilize essas funcionalidades conforme necessário para administrar e analisar as postagens em seu fórum, garantindo um controle efetivo sobre o conteúdo e oferecendo insights adicionais sobre a atividade dos usuários.
