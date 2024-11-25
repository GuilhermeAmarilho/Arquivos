import speech_recognition as sr # type: ignore

microfone = sr.Recognizer()
# Aqui mostra todos os microfones
# print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
    microfone.adjust_for_ambient_noise(mic)
    #Avisa ao usuario que esta pronto para ouvir
    print("Pode falar que eu vou gravar")
    #Armazena a informacao de audio na variavel
    audio = microfone.listen(mic)
    #Passa o audio para o reconhecedor de padroes do speech_recognition
    texto = microfone.recognize_google(audio, language="pt-BR")
    #Após alguns segundos, retorna a frase falada
    print(type(texto))
    print(texto)
