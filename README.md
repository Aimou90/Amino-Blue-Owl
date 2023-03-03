# Amino-Blue-Owl  <img width="25" src="https://upload.wikimedia.org/wikipedia/commons/1/1f/Amino_icon.jpg">
- Solução para poder proteger seu chat contra flood/trava!

<div>

## Introdução!
Há pessoas Bibliotecas que interajam com a API do Amino que, apesar do desenvolvedor pensar como forma de solução para suas automações seja para estudo, diversão ou gestão, existem aqueles que utilizam de forma mal intencionada. Logo, fazendo aqueles que são leigos no assunto terem uma imagem muito distorcida do projeto (já que, quando se fala de script no Amino, a primeira coisa que falam é: "Script funciona pra travar chat" ou "Script é um bot que convida pessoas para uma chamada de forma indevida"). Essas pessoas mal intencionadas utilizam desse projeto para travar os chats das comunidades do Amino, causando prejuízo na comunicação dos usuários. Como forma de solução para lidar com esses tipos de pessoas dentro da plataforma, foi criado esse projeto com a contribuição da Oceanos (Clã da Otanix) para distribuir a público esse projeto.

O Blue Owl foi desenvolvido especificamente para a proteção dos chats da Oceanos, mas foi decidido ser distribuído para o público para todos poderem usar. Isso foi pensado, pois nem todos são capazes de se protegerem. Logo, sendo vítimas de travas sem a chance de se defender.

## Como Usar? Linux - (Terminal/Termux)
A principio, é sempre bom você atualizar seus repositórios, então utilize o gerenciador de pacotes do seu terminal para atualizar seus pacotes

#### Demonstração - Como funciona
<a href="https://youtube.com/shorts/hIDLG5__ZT0?feature=share"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" align="center"/></a>

### Debian Based (Ubuntu, ZorinOS, Linux Mint) ou Termux
```
$ apt update && apt upgrade -y
```
### Fedora/RedHat
```
$ dnf update
```
### ArchLinux
```
$ pacman -Syu
```

Após atualizar seu repositório, você deve fazer a instalação do Python e Git utilizando seu gerenciador de pacote, logo, clonando esse repositório, acessando o diretório do projeto, instalando os requerimentos e executando o script.
```
$ git clone https://github.com/MrWestOFC/Amino-Blue-Owl
$ cd Amino-Blue-Owl
$ pip install -r requirements.txt
$ python main.py
```

## Nota!
Deve conter um arquivozinho em json, nomeado de 'config', é por lá que você irá colocar seu email, senha e o ID da comunidade que você deseja gerenciar seus chats, mas se você executar o script sem o arquivo, ele criará um novo e você pode editar sem perder a produtividade. O Arquivo em Json conterá esses seguintes endpoints:
```json
{
    "Project": "Blue Owl Lite - MrWest",
    "Author": "Mister West",
    "Description": "Descrição do Projeto",
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
```
 
## Auxiliar
Existe um auxiliar dentro do repositório em que você poderá retornar o comID de uma comunidade pelo ID do Amino.
```
python aux.py
```
## Posso usar no Pydroid?
Sim, você pode executar o script tranquilamente no Pydroid, basta você baixar o arquivo em python do projeto e utilizar tranquilamente. O auxiliar é opcional, já que ele é só um adicional para você conseguir capturar ID de comunidade, mas ele também utiliza o config.json para poder logar em sua conta

#### Demonstração - Processo de Download para Pydroid
<a href="https://youtube.com/shorts/e-uynda5UwM?feature=share"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" align="center"/></a>
<div/>
  
