===============
EnigmaRPG-ficha
===============

Este repositório traz o criador de ficha para o RPG Enigma.


Instalação
==========

Por enquanto ele não tem um instalador nem interface gráfica, então para utiliza-lo é necessário executar por linha de comando.

Requisitos
----------
- Python (preferencialmente > 3.8)

Download ou clone o repositório
-------------------------------

.. code-block:: shell

    $ git clone https://github.com/marujore/EnigmaRPG-ficha.git

Entre no diretório:

.. code-block:: shell

    $ cd EnigmaRPG-ficha

Crie um ambiente Python separado no qual serão instaladas as dependências (opcional)
------------------------------------------------------------------------------------

Você pode usar Conda ou Venv para criar ambientes isolados

Ambiente com Conda (requer Conda instalado)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crie um novo ambiente

.. code-block:: shell

    $ conda create --name enigma python=3.8

Ative o ambiente

.. code-block:: shell

    $ conda activate enigma

Ambiente com Venv (requer Venv instalado)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crie um novo ambiente

.. code-block:: shell

    $ python3 -m venv venv

Ative o ambiente

.. code-block:: shell

    $ source venv/bin/activate
Instale os pacotes necessários
------------------------------

.. code-block:: shell

    $ pip3 install .[all]

Uso
===

Criação de Nova Ficha
---------------------

