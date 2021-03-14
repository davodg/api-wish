<h1 align="center">
  <a href="https://apiwish.herokuapp.com/">Api Wish</p>
</h1>

<p align="center">Uma API para gerir uma wishlist desenvolvida usando Python</p>

### Features

- [x] Cadastro e autenticação de usuário
- [x] Cadastrar, alterar, e deletar itens da wishlist
- [x] Visualizar a lista dos itens cadastrados de forma completa ou randomicamente um item

<h1 align="center">Utilização</h1>

<p align="center">Antes de cadastrar um item na wishlist, é necessário criar um usuário e fazer o login</p>
<p align="center">Para registrar um usuário basta clicar em "try it out" no método POST de api/auth/register, modificar os campos e executar</p>

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scregister.png" />
</h1>

<p align="center">Para fazer o login, é necessário usar o método POST de api/auth/login e colocar o username e senha cadastrados</p>

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scrlogin.png" />
</h1>

<p align="center">Após isso, será mostrado um token no resultado do login, para autenticar é necessário copiar o token, e colocá-lo em "Authorize" da mesma forma que está descrito na imagem</p> 

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scrauthorize.png" />
</h1>

<p align="center">Depois de autenticar, é possivel adicionar um item na wishlist, para isso basta usar o método POST de /wishes/ e modificar os campos de acordo com o desejado</p> 

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scrwishpost.png" />
</h1>

<p align="center">Para visualizar os itens cadastrados, é usado o método GET de /wishes/</p> 

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scrwishget.png" />
</h1>

<p align="center">E para modificar os dados de um item cadastrado é usado o método PUT de /wishes/, mudar os campos desejados e passar o id do item que será modificado</p> 

<h1 align="center">
  <img alt="Register" title="Register" src="./assets/scrwishput.png" />
</h1>

<p align="center">O endpoint /random/ retorna aleatóriamente um item da lista</p>
<p align="center">E para deletar um item basta usar o método DELETE de /wishes/ e passar o id do item a ser deletado</p>
