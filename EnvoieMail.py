# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:41:51 2021

@author: Administrator
"""

from selenium import webdriver
from time import sleep
import getpass
from selenium.webdriver.common.keys import Keys
from donnees import * # C'est ici que ce trouve les chaines de caratères non déclarées (identifiant, motdepasse, destinataire, corpus, objet, chemin)

driver = webdriver.Chrome('H:\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://mail.google.com")

########## Connexion à Gmail ##########
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(identifiant)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(motdepasse)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
#######################################
sleep(5)
# Fermeture de la fenêtre des notifications (cette fenêtre gène par la suite)
try :
    driver.find_element_by_xpath('//*[@id="link_enable_notifications_hide"]').click()
except:
    pass
# On commence un nouveau message
driver.find_element_by_xpath("//*[contains(text(), 'Nouveau message')]").click()

sleep(3)

########## Ecriture du message ##########
driver.find_element_by_css_selector('textarea[aria-label="À"]').send_keys(destinataire)
driver.find_element_by_css_selector('div[aria-label="Corps du message"]').send_keys(corpus)
driver.find_element_by_css_selector('input[aria-label="Objet"]').send_keys(objet)
# Ajouter une pièce jointe
driver.find_element_by_css_selector('input[type="file"][name="Filedata"]').send_keys(chemin)
#########################################

#On envoie
driver.find_element_by_css_selector('div[aria-label="Envoyer ‪(Ctrl-Enter)‬"]').click()
