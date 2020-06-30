<h1 align="center">VotoSensato</h1>
<p><h3 align="center">Projeto de um site que utliza Vue.js no frontend e Flask no backend.</h3></p>
<br>
<h3>Introdução :clipboard:</h3>
  <p> O site oferece um sistema de busca de deputados ativos na câmara dos deputados pelo seu partido e estado, além de mostar um resumo do partido dentro da câmara, como o número de deputados que possui lá dentro e sua situação. A mini-api desenvolvida consome dois serviços externos e formata os dados enviados por estes  para ser utilizado corretamente pelo site.</p>
 <br>
 <h3>Techs utilizadas :rocket:</h3>
  <ul>
    <li>
      <h4>Front-end</h4>
      <ul>
        <li>Vue.js</li>
        <li><a href="https://github.com/axios/axios">Axios<a></li>
        <li><a href="https://github.com/wyzantinc/vue-radial-progress">Vue-radial-progress</a></li>
      </ul>
   </li>
   <li>
      <h4>Back-end</h4>
      <ul>
        <li>Flask</li>
        <li>
          Serviços externos
          <ul>
            <li><a href="https://servicodados.ibge.gov.br/api/docs/localidades?versao=1">IBGE</a></li>
            <li><a href="https://dadosabertos.camara.leg.br/swagger/api.html">Dados abertos da câmara dos deputados do Brasil</a></li>
          </ul>
        </li>
     </ul>   
   </li>  
  </ul>
 <br>
<h3>Rodando aplicação</h3>
Primeiramente clone o projeto :

```
  git clone https://github.com/arthur-andraade/VotoSensato.git
```

<h4><strong>Back-end</strong></h4>
<p>Para testar a mini-api construída em Flask é necessário ter em sua máquina o python instalado, e com ele instalar o <strong>virtualenv</strong>. Comando para instalar virtualenv :</p>

```
  pip install virtualenv
```
<p>Com pacote instalado, crie uma virtualenv com sequinte comando :</p>

```
virtualenv nome_da_virtualenv
```
É recomendável que virtualenv criada esteja no meu diretório raíz do projeto.
<p>Após cria-lá é necessário ativa-lá para instalar das dependências que a aplicação utiliza, o comando para isto difere em cada sistema operacional.</p>
<p>Windows :</p>

```
  nome_da_virtualenv/Scripts/activate.bat
```

<p>Linux ou MacOS : </p>

```
  source nome_da_virtualenv/bin/activate
```
Com virtualenv ativada, agora é necessário instalar os pacotes que a aplicação necessita, para isto rode o comando :

```
  pip install -r requirements.txt
```
Após instalar as dependências, rode o comando a seguir
para rodar a mini-api :

```
  flask run
```
Agora a mini-api estará rodando em determinada porta de sua máquina e estará disponível para receber os **requests** e enviar dados para o front-end.
<br>
<h4><strong>Front-end</strong><h4>
<p> Para rodar parte do front-end é necessário ter instalado em sua máquina o NPM para instalar o vue-cli com seguinte comando : </p>

```
  npm install -g @vue/cli
```
A seguir instale dependências utilizadas no projeto com seguinte comando :

```
  npm install 
``` 
E por fim rode o comando para subir a aplicação do front-end com o comando :
```
  npm run serve
```
<p>Para visualizar a aplicação entre no seu browser e coloque o endereço aonde a aplicação está rodando.</p>
<br>
<br>
<div align="center">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/arthur-andraade/VotoSensato?style=social">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/arthur-andraade/VotoSensato">
</div>
