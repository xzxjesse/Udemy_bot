from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#chave: Rrhn5srkkpY2zxzdirqW9x8DOcvfDji4
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/Rrhn5srkkpY2zxzdirqW9x8DOcvfDji4", headers=agent, verify=False)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()

#abrir e salvar wpp
dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options=chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
    #abrir as notificações
        
        #l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt
        #bolinha = driver.find_element(By.CLASS_NAME, 'aumms1qt')
        #bolinha = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
        
        #API
        bolinha = driver.find_element(By.CLASS_NAME, bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME, bolinha_notificacao)
                
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(2)
        
    #pegar contato
        
        #telefone_cliente = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')
        
        #API
        telefone_cliente = driver.find_element(By.XPATH, contato_cliente)

        telefone_final = telefone_cliente.text
        print(telefone_final)
        time.sleep(2)
        
    #capturar mensagem do contato
        
        todas_as_mensagens = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_mensagens_texto = [e.text for e in todas_as_mensagens]
        mensagens = todas_as_mensagens_texto[-1]
        print(mensagens)
        time.sleep(2)      
        
    except:
        print('ola')
        
while True:
    bot()
