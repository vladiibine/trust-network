# trust_network_backend
> Python Tornado SQL Alchemy (async maybe) backend

[![Build Status][travis-image]][travis-url]

The tornado based SQL Alchemy backend for the coolest app ever, implementing a trust network

![](header.png)

## Instalação

**Dependências**

* Python3

Linux (debian):

```sh
apt-get install $(cat requirements.apt)
```

## Exemplo de uso

Alguns exemplos motivamentes e úteis sobre como seu projeto pode ser utilizado. Adicionei blocos de códigos e, se necessário, screenshots.

## Configuração para Desenvolvimento

Crie e ative um ambiente virtual no diretório raiz do projeto
```sh
mkvirtualenv trust_network_backend
```

Configure as variáveis de ambiente
```sh
cd trust_network_backend
cp rename-as.env .env
```
Edite o arquivo `.env` e incluia as variáveis de ambiente.

Instalação das dependências do projeto
```sh
make install-dev
```

Testes
```sh
make test
```

Localserver
```sh
make runserver
```

## Deploy

Sandbox

Deploy realizado no Tsuru
```sh
make deploy-sandbox
```

## Changelog

* 0.2.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 0.2.0
    * MUDANÇA: Remove `setDefaultXYZ()`
    * ADD: Adiciona `init()`
* 0.1.1
    * CONSERTADO: Crash quando chama `baz()` (Obrigado @NomeDoContribuidorGeneroso!)
* 0.1.0
    * O primeiro lançamento adequado
    * MUDANÇA: Renomeia `foo()` para `bar()`
* 0.0.1
    * Trabalho em andamento

## Meta

Ardelean Vlad George

Distribuído sob a licença XYZ. Veja `LICENSE` para mais informações.

[https://github.com/yourname/github-link](https://github.com/othonalberto/)

[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/vladiibine/trust_network_backend
[brew]: http://brew.sh/
[pyenv]: https://github.com/yyuu/pyenv
