#coding: utf-8

import aminofix
import json
import os

from threading import Thread

try:
  with open(os.path.dirname(os.path.realpath(__file__)) + "/config.json") as end_point:
    endpoint = json.load(end_point)
    owl = endpoint['blueowl']

    client = aminofix.Client()
    
    # Função que iniciará tudo
    def start_close_chat():
      try:
        sub_client = aminofix.SubClient(comId=owl['community']['comid'], profile=client.profile)
        chats = sub_client.get_chat_threads(start=0, size=100)

        while True:
          try:
            print("> > > > . . .")
            # Imprimir todos os seus chats dentro da comunidade
            for x, y in enumerate(chats.title, 1):
              print("\033[36m" + f"{x} " + "" + "\033[33m" + f"{y}")
              
            # Selecionar seu chat para ser fechado
            print("\033[36m" + "0 " + "\033[33m" + "Todos")
            chat_selected = int(
              input("\033[32m" + "Selecione um chat >> " + "\033[33m"))
            chat_id = chats.chatId[chat_selected - 1]

            try:
              if chat_selected != 0: # Fechar um chat a sua escolha
                print("\033[36m" + "Fechando o chat..! " + "\033[37m")
                sub_client.edit_chat(chatId=chat_id, viewOnly=True)
              else: # Fechar todos os chats se caso digitar "0"
                print("\033[32m" +
                      "Todos os chats serão Fechados pelo Coruja" + "\033[37m")
                for x in chats.chatId: 
                  # x = Reberá todos os ID dos chats que serão fechados
                  # viewOnly = Se verdadeiro (True) o chat será fechado
                  
                  try:
                    sub_client.edit_chat(chatId=x, viewOnly=True)
                    print("\033[33m" + f"{x} " + "\033[36m" + "Fechado" +
                          "\033[37m")
                  except aminofix.lib.util.exceptions.ActionNotAllowed:
                    print("\033[33m" + f"{x}" + "\033[31m" + " Sem Perm." +
                          "\033[37m")
                  except Exception:
                    pass
                  
            except aminofix.lib.util.exceptions.ActionNotAllowed as err:
              print(
                "\033[31m" + "Você não tem Permissão nesse chat - \n" +
                "- EndPoints:\033[37m", err)
            except Exception:
              pass

          except IndexError:
            print("\033[31m" + "Chat não listado - " + "\033[37m")
          except ValueError:
            print("\033[31m" + "Valor Incorreto" + "\033[37m")
          except TypeError:
            print("\033[31m" + "Valor Incorreto" + "\033[37m")

      # Maioria dos casos, essa exceção é devido ao dispositivo não suportar a versão
      # Devido a falta de parâmetros. Se esse erro persistir por mais que esteja tudo correto
      # é devido a biblioteca "amino.fix" está obstoleta
      
      except aminofix.lib.util.exceptions.UnsupportedService as err:
        print("Certifique que não faltou alguma informação da 'config.json'")
        
    # Inicialização do Script
    if __name__ == "__main__":
      try:
        client.login(email=owl["account"]["email"],
                     password=owl["account"]["passwd"])
        
        # Ininio da função de forma paralela
        Thread(target=start_close_chat()).start()

      except aminofix.lib.util.exceptions.InvalidAccountOrPassword as err:
        print(
          "\033[31m" +
          "Email ou Senha está incorreta! - Pressione 'CTRL + C' PARA SAIR\n" +
          "- EndPoints:\033[37m", err)
      except aminofix.lib.util.exceptions.InvalidPassword as err:
        print(
          "\033[31m" +
          "Email ou Senha está incorreta! - Pressione 'CTRL + C' PARA SAIR\n" +
          "- EndPoints:\033[37m", err)
      except aminofix.lib.util.exceptions.AccountDoesntExist as err:
        print(
          "\033[31m" +
          "Essa conta não existe! - Pressione 'CTRL + C' PARA SAIR\n" +
          "EndPoints:\033[37m", err)
       except aminofix.lib.util.exceptions.VerificationRequired as err:
        print(
          "\033[31m" +
          "Verificação requirida! - Acesse o link retornado pelo endpoint para verificar" +
          "EndPoints:\033[37m", err
        )
      # End
except FileNotFoundError:
  print("O arquivo 'config.json' não encontrado, criando...")
  aDict = {
    "Project": "Blue Owl Lite - MrWest",
    "Author": "Mister West",
    "Description":
    "Bot criado com objetivo de fechar seus chats de forma que não seja afetado pela trava de um flood",
    "blueowl": {
      "account": {
        "email": "",
        "passwd": ""
      },
      "community": {
        "comid": ""
      }
    }
  }

  jsonString = json.dumps(aDict, indent=4)
  jsonFile = open("config.json", "w")
  jsonFile.write(jsonString)
  jsonFile.close()
  print("Concluído! Digite CTRL + C e edite o arquivo")

  # End
