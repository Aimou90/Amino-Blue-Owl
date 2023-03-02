# Amino-Blue-Owl  <img width="25" src="https://upload.wikimedia.org/wikipedia/commons/1/1f/Amino_icon.jpg">
- Solução para poder proteger seu chat contra flood/trava!

<div>

## Introdução!
Há pessoas Bibliotecas que interajam com a API do Amino que, apesar do desenvolvedor pensar como forma de solução para suas automações seja para estudo, diversão ou gestão, existem aqueles que utiliza de forma mal intencionada, logo fazendo aqueles que são leigos no assunto terem uma imagem muito distrocida do projeto (já que quando se fala de script no amino a primeira coisa que falam é: "Script funciona pra travar chat" ou "Script é um bot que convida pessoas para uma chamada de forma indevida"). Essas pessoas mal intencionadas utilizam desse projeto para travar os chats das comunidades do amino, causando prejuízo na comunicação de usuários. Como forma de solução para lidar com esses tipos de pessoas dentro do amino, foi criado esse projeto, com a contribuição da <strong>Oceanos</strong> (Clâ da Otanix) para distribuir a publico esse projeto.

O Blue Owl foi desenvolvido especificamente para a proteção dos chats da Oceanos, mas foi decidido ser distribuido para o público para todos poderem usar. Isso foi pensado pois nem todos são capazes de se protegerem, logo sendo vítimas de travas, sem a chance de se defender.
 
## Como Usar? Linux - (Terminal/Termux)
A principio, é sempre bom você atualizar seus repositórios, então utilize o gerenciador de pacotes do seu terminal para atualizar seus pacotes

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

Após atualizar seu repositório, você deve fazer a instalação do Python e Git utilizando seu gerenciador de pacote, logo, clonando esse repositório, acessando o diretório do projeto e executando o script
```
$ git clone https://github.com/MrWestOFC/Amino-Blue-Owl
$ cd Amino-Blue-Owl
$ python main.py
```

## Nota!
- Deve conter um arquivozinho em json, nomeado de 'config', é por lá que você irá colocar seu email, senha e o ID da comunidade que você deseja gerenciar seus chats. O Arquivo em Json conterá esses seguintes endpoints:
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
<div/>
  
