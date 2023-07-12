# pykeylog
Keylogger em Python, feito da forma mais simples possível para copiar as teclas pressionadas e enviar a cada 12 horas para o e-mail do atacante.
# Como usar:
Altere EMAIL_ADDRESS = "youremail@example.com" e EMAIL_PASSWORD = "yourpassword"
Você também pode alterar o intervado de tempo que o e-mail será enviado com as teclas pressionadas em: SEND_REPORT_EVERY = 43200  # (seconds)
No meu caso, para não ficar chegando muitos emails, coloquei para receber a cada 12 horas. Use sempre em segundos.
# Lembre-se:
Importar as bibliotecas:
smtplib
pynput
threading
email.mime.text
# USE COM RESPONSABILIDADE!

# Transformar em .exe
Após a finalização do script, utilizei auto_py_to_exe para transformar o arquivo py em exe.
Enjoy
