# CLEO — Central Listing for Easy Ordering
- Esse repositório contém o código fonte completo do nosso Software.
>- Versão 3.0 já disponível: <a href="http://cleo-v2-env.eba-qr2tnipv.sa-east-1.elasticbeanstalk.com/">CLEO — Central Listing for Easy Ordering</a>

## Objetivo do Projeto
- CLEO é uma aplicação web para desburocratizar, agilizar e tornar mais eficiente o acesso aos produtos da Cantina da CESAR School BRUM. A solução busca reduzir o desconforto das filas de espera sob o calor do sol e trazer mais comodidade aos clientes da cantina. Junto à CLEO, a cantina irá registrar seus produtos para que os alunos e funcionários da CESAR possam fazer seus pedidos, assim como realizar o pagamento dos mesmos, de forma antecipada, por meio da aplicação web. Quando o pedido estiver pronto ou separado o cliente apenas terá que se locomover ao balcão para realizar a retirada.

## Linguagens e Frameworks utilizados
- Back-end: Python (Django)
- Front-end: HTML, CSS e Javascript

## Instalação
1. **Criar Ambiente Virutal**
>- MacOS/Linux: `python3 -m venv venv`
>- Windows: `python -m venv venv`

2. **Ativar ambiente virtual**
>No diretório da pasta "venv" (criado acima):
>- MacOS/Linux: `source venv/bin/activate`
>- Windows: `venv/Scripts/activate`

3. **Clonar repositório CLEO**
>Com o ambiente "venv" ativado:
>- `git clone https://github.com/theomilll/CLEO`

4. **Configurar ambiente virtual**
>Após clonar o repositório em sua máquina:
>- MacOS/Linux: `pip3 install -r requirements.txt`
>- Windows: `pip install -r requirements.txt`

5. **Iniciar o servidor local**
>Após configurar ambiente com os requisitos necessários:
>- MacOS/Linux: `python3 manage.py runserver`
>- Windows: `python manage.py runserver`

6. **Abrir projeto CLEO**
>Após iniciar o servidor, clickar no link disponibilizado no terminal:
<div align="center">
  <img src="https://user-images.githubusercontent.com/108446826/232560661-522de845-7aa1-425b-93cd-7526af1a3bcb.png" title="Visão do Terminal" alt="Visão do Terminal" width="500px"/>
 </div>

7. **Teste de Sistema (E2E) Automatizados**
> Para a instalação do selenium:
>- Digite no seu terminal `pip install selenium`;
>- Faça a verificação de qual versão é o seu google chrome;
>- Feita a verificação, faça o download que condiz a versão do seu google chrome, através do link: https://sites.google.com/chromium.org/driver/downloads?authuser=0
>- No VsCode (ou IDE utilizada), na pasta ‘main’, crie uma pasta com o nome de ‘selPath.py’;
>- Dentro da pasta criada, crie a variável ‘SELENIUM_DIRS’, passando a url do chrome drive instalado para essa variável.

## Link do Jira
- Acompanhe o desenvolvimento: <a href="https://mffbm.atlassian.net/jira/software/projects/FDS/boards/1">CLEO Jira Board</a>

## Link do Figma
- Acompanhe os protótipos: <a href="https://www.figma.com/file/gsZa5WDhVrfWIilATY4K0P/LO-FI-CLEO?node-id=0%3A1&t=VpvNaYuTkpGkrmfp-1">Protótipo Lo-Fi CLEO</a>

## Diagrama de atividades
><a href="https://drive.google.com/file/d/1FabeMVBPQQIfxzVGJYi8imu3IjyhV-j2/view?usp=sharing">*Acesse aqui o Diagrama de Atividades CLEO em .pdf.*</a>
<div align="center">
<img src="https://github.com/theomilll/CLEO/assets/108446826/d78ab9af-ff45-41af-ba5a-21aaf704779a" title="Diagrama de Atividades CLEO" alt="Diagrama de Atividades CLEO" width="900px"/>
</div>

## Relato Programação em Pares (Pair Programming)
><a href="https://docs.google.com/document/d/19kMGlKWTtmS4_a0b0ogvFF-unXA4oes1-lSFioI59Ns/edit?usp=sharing">*Acesse aqui os relatos completos.*</a>
### Sprint 1
- *"Indubitavelmente a prática do Pair Programming é um dos motivos pela satisfação da equipe e pelos bons resultados vistos ao final da Sprint 1. Por meio dela, foi possível distribuir o conhecimento a respeito dos recursos utilizados e do produto desenvolvido, de forma que todos se mantivessem à parte e compreendendo o todo ao realizar suas tarefas, o que resultou em um produto desenvolvido de forma mais eficiente, com menos erros, mais consciência e melhores experiências."*
### Sprint 2
- *"Acreditamos que, mesmo levantando dificuldades, a experiência da programação em pares nesta Sprint 2 revelou muitos pontos de melhoria, o que aumentou, está aumentando e certamente aumentará a qualidade do nosso projeto, assim como reforçou a comunicação e o sentimento de equipe entre os integrantes."*
### Sprint 3
- *"Encerramos a terceira e última sprint de forma positiva, com a equipe mais sincronizada e unida do que nunca. Foi uma ótima experiência trabalhar como equipe, aprendendo um com os outros, desenvolvendo um projeto de qualidade e fomentando amizades, experiência essa que certamente foi influenciada pela utilização da programação em pares."*

## Integrantes da Equipe
- <a href="mailto:abxa@cesar.school">Ana Beatriz Alves</a>
- <a href="mailto:cba2@cesar.school">Caio Barreto</a>
- <a href="mailto:cm2@cesar.school">Cristina Matsunaga</a>
- <a href="mailto:mffbm@cesar.school">Maria Fernanda Marques</a>
- <a href="mailto:hrm@cesar.school">Henrique Roma</a>
- <a href="mailto:tam4@cesar.school">Théo Moura</a>
