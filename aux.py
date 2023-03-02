#coding: utf-8

import aminofix
import json
import os

try:
  with open(os.path.dirname(os.path.realpath(__file__)) +
            "/config.json") as end_point:
    point = json.load(end_point)
    owl = point['blueowl']

    client = aminofix.Client()

    def search_com():
      while True:
        try:
          comid = (input("Digite o ID do Amino > "))
          r = client.search_community(comid)
          print(f"ID da comunidade: {r.comId}")
        except aminofix.lib.util.exceptions.CommunityNotFound:
          print("Comunidade não encontrada")
        except KeyboardInterrupt:
          print("Processo Interrompido. Digite mais uma vez CTRL + C")
          exit()

    try:
      client.login(email=owl['account']['email'],
                   password=owl['account']['passwd'])
      search_com()

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
        "Verificação requirida! - Acesse o link retornado pelo endpoint para verificar"
        + "EndPoints:\033[37m", err)

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

  json_dict = json.dumps(dict, indent=4)
  file_config_json = open("config.json", "w")
  file_config_json.write(json_dict)
  file_config_json.close()
  print("Concluído! Digite CTRL + C e edite o arquivo")
  # End
