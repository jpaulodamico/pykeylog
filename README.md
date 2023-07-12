# Keylogger Simples em Python

Este repositório contém um script de keylogger simples escrito em Python. Ele registra todas as teclas pressionadas no teclado e envia um relatório via e-mail em intervalos regulares.

## ⚠️ Aviso Legal

O uso de um keylogger é legalmente e eticamente questionável. Este código é fornecido apenas para fins educacionais e não deve ser usado para atividades mal-intencionadas. Nunca use este código sem o consentimento explícito do proprietário do computador onde ele está sendo executado.

## 🚀 Como executar

1. Instale as dependências necessárias com o comando:

    ```shell
    pip install pynput==1.7.4
    ```

2. Substitua as constantes `EMAIL_ADDRESS` e `EMAIL_PASSWORD` no script `keylogger.py` pelas suas informações de login de e-mail.

3. Execute o script `keylogger.py`:

    ```shell
    python keylogger.py
    ```

## ⏱️ Configuração do intervalo de relatório

Por padrão, o script envia um relatório por e-mail a cada 12 horas. Você pode alterar este intervalo modificando a constante `SEND_REPORT_EVERY` no script `keylogger.py`. O valor é especificado em segundos.

## 📧 Configuração do e-mail

O script está configurado para usar o servidor SMTP do Outlook.com para enviar e-mails. Se você estiver usando um provedor de e-mail diferente, você precisará alterar o host e a porta na chamada `smtplib.SMTP` na função `sendmail`.

## 🔑 Senha do aplicativo

Se você ativou a verificação em duas etapas na sua conta de e-mail, você precisará gerar uma senha de aplicativo para usar no script. Você pode fazer isso através da página de segurança da sua conta de e-mail.

## 📋 Formato do log de teclas

O script registra cada pressionamento de tecla como um caractere na string de log. Teclas especiais (como espaço, enter, e teclas de função) são registradas como palavras entre colchetes (por exemplo, `[ENTER]`, `[SPACE]`). O script envia esta string de log como o corpo do e-mail de relatório.

## 📄 Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
