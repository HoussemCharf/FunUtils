#!/usr/bin/python3
# por Lucas Carrafa
import smtplib
import os
import commands
from email.mime.text import MIMEText
import time

def envia_email(texto):
	informacao = "A velocidade da rede esta em " + str(texto) +" Mbit/s" #corpo do email
	
	msg = MIMEText(informacao)
	msg['Subject'] = "Velocidade da rede!"
	msg['From'] = "email remetente"
	msg['To'] = "email destino"

	server = smtplib.SMTP('smtp.gmail.com', 587) #servidor de email SMTP, nesse exemplo Gmail
	server.starttls()
	server.login("inserir um email", "senha")

	server.sendmail("email remetente","email destino", msg.as_string())
	server.quit()


def verifica_rede(): #executa no shell um comando e retorna o resultado
	return commands.getstatusoutput("speedtest-cli") 

def retira_dados(dado): #funcao que pega apenas a velocidade
	ini = "Download: "
	fim = " Mbit/s"
	tam = len(ini)
	p_ini = dado.find(ini) + tam
	p_fim = dado.find(fim)
	return dado[p_ini:p_fim]

#_____________MAIN_______________#

while True:
	aux = verifica_rede()
	envia_email(retira_dados(aux[1]))
	time.sleep(43200) #aguarda 12 horas para enviar o proximo