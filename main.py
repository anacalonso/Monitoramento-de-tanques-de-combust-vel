import RPi.GPIO as GPIO
import time
import requests

# Configurações do ThingsBoard
THINGSBOARD_HOST = 'demo.thingsboard.io'  # Alterar para seu servidor do ThingsBoard
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'        # Substitua pelo token do dispositivo no ThingsBoard

# Configurações do sensor ultrassônico
TRIG_PIN = 23  # GPIO23
ECHO_PIN = 24  # GPIO24

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def medir_distancia():
    # Envia um pulso de 10µs para o pino TRIG
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Espera o retorno do ECHO
    while GPIO.input(ECHO_PIN) == 0:
        inicio_pulso = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        fim_pulso = time.time()

    # Calcula a duração do pulso
    duracao_pulso = fim_pulso - inicio_pulso

    # Converte a duração em distância (em cm)
    distancia = duracao_pulso * 17150
    distancia = round(distancia, 2)
    
    return distancia

def calcular_nivel(distancia, altura_tanque):
    # Calcula o nível do tanque em percentual
    nivel = ((altura_tanque - distancia) / altura_tanque) * 100
    nivel = max(0, min(100, nivel))  # Garante que o nível esteja entre 0% e 100%
    return round(nivel, 2)

def enviar_dados_ao_thingsboard(nivel):
    url = f'http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry'
    payload = {'nivel_combustivel': nivel}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Dados enviados com sucesso para o ThingsBoard.")
        else:
            print(f"Falha ao enviar dados: {response.status_code}")
    except Exception as e:
        print(f"Erro na conexão com o ThingsBoard: {str(e)}")

def main():
    altura_tanque = 100.0  # Altura do tanque em cm (deve ser ajustada conforme o tanque real)

    try:
        while True:
            distancia = medir_distancia()
            print(f"Distância medida: {distancia} cm")
            
            nivel = calcular_nivel(distancia, altura_tanque)
            print(f"Nível de combustível: {nivel}%")
            
            enviar_dados_ao_thingsboard(nivel)
            
            time.sleep(60)  # Espera de 1 minuto antes da próxima leitura
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
