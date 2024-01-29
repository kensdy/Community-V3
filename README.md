# Community-V3

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

Certamente, aqui está uma melhoria para essa seção:

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
  
Para melhorar essa descrição, você pode considerar a seguinte versão:

### Gerenciamento de Dados

No arquivo `data.json`, a base de dados de posts é armazenada, oferecendo funcionalidades de gerenciamento essenciais. Além de conter informações sobre as postagens, este arquivo proporciona recursos adicionais:

#### 1. **Apagar Postagens:**
   - Através do arquivo `data.json`, é possível excluir postagens conforme necessário. Basta localizar a entrada correspondente e removê-la do arquivo para realizar a exclusão.

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
            "timestamp": "
Data, hora e microssegundos",
            "comments": [
                {
                    "author": "Nome do Autor",
                    "content": "Conteúdo do Comentário"
                    "ip_address: "192.168.0.1"
                }
            ]
            "ip_address: "192.168.0.1"
        }
    ]
}
   ```

#### 3. **Rastreamento de IP:**
   - O campo `user_ip` em cada entrada permite rastrear o IP do autor da postagem, oferecendo uma camada adicional de informação sobre a origem das interações no seu site.

Utilize essas funcionalidades conforme necessário para administrar e analisar as postagens em seu fórum, garantindo um controle efetivo sobre o conteúdo e oferecendo insights adicionais sobre a atividade dos usuários.
