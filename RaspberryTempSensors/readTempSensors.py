#!/usr/bin/python
# coding=utf-8
#----------------


import os, sys, time
import mysql
import mysql.connector
import urllib2

try:
    connection = mysql.connector.connect(host = "localhost", user= "myuser", passwd = "mypassword", db = "mydb")
except:
    print "No Connection"
    exit(0)

# read temp   
def aktuelleTemperatur():
      
    # 1-wire Slave Datei lesen 28-0416c4de55ff
    file = open('/sys/bus/w1/devices/28-0416c4de55ff/w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000

    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

# Raum Temperatur auslesen
def aktuelleTemperatur2():
      
    # 1-wire Slave Datei lesen 28-0416c4d03fff
    file = open('/sys/bus/w1/devices/28-0416c4d03fff/w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvaluee = filecontent.split("\n")[1].split(" ")[9]
    temperaturee = float(stringvaluee[2:]) / 1000

    # Temperatur ausgeben
    rueckgabewert2 = '%6.2f' % temperaturee 
    return(rueckgabewert2)

schleifenZaehler = 0
schleifenAnzahl = 1

while schleifenZaehler < schleifenAnzahl:
    messdaten = aktuelleTemperatur()
    messdaten2 = aktuelleTemperatur2()
    
    # Schleifenzähler erhöhen
    schleifenZaehler = schleifenZaehler + 1

    # Temperatur in lokale Datenbank schreiben
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (temp1, temp2) VALUES (%s, %s)",(messdaten, messdaten2,))
    cursor.close
    connection.commit()