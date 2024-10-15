# EditoraDinamica

Rafael Feliciano e Lucas Ebrenz

DOCKER: COMO USAR A IMAGEM GERADA, ENVIADA AO PROFESSOR ? 

sudo docker pull miyaaaa/django-docker:0.0.1

sudo docker run -d -p 8000:8000 miyaaaa/django-docker:0.0.1

/* talvez necessário */
sudo docker start  |idCONTAINER do trabalho encontrado em "sudo docker ps -a"| 

======================================================================================================================================================
O tempo não permitiu que implementássemos a parte atrelada a revisor.

Página inicial !
Visão do leitor e usuário não logado: a página inicial exibe todos os livros, suas categorias e clicar em uma capa leva a algum lugar e letras aparecem além da imagem por razão desconhecida.  Exibe opção de login e aviso de não estar logado. O clique para fazer login leva à pagina de login.  O admin consegue sair de sua conta nessa paǵina, assim como criar e ver todos livros. O escritor tem seu cargo de escritor mencionado na página assim como botão de sair para fazer logout na mesma. Os livros escritos por ele aparecem nessa página e o de mais nenhum outro autor. Ele pode criar livros.

Página do livro !
Visão do leitor e usuário não logado: Titulo, categoria, capa, autor, sinopse e um link para o capítulo o qual o usuário quer ler estão presentes. O administrador pode criar novo capítulo, excluir e deletar livros de quaisquer usuários. O escritor pode fazer o que o administrador pode, mas apenas quanto a seus livros.
Campo texto para titulo, botões para selecionar autor, categoria e capa. Campo texto para sinopse do livro e botão de enviar formulário para criar novo livro.

Página capítulo !
Visão do leitor e usuário não logado: O capítulo desejado está exposto e para voltar a tela do livro basta clicar no botão de voltar, no navegador. O administrador pode editar e criar capítulos de quaisquer livros. O escritor pode fazer o que o administrador pode, mas apenas quanto a seus livros.

Página de criação de capítulo !
O administrador pode criar capítulo para qualquer usuário
O escritor pode escrever capítulos para seus livros e por uma falha de tempo na implementação pode também criar capítulos para outros livros.
Leitor/usuário não cadastrado: não possuem acesso a essa página. Logo, ficam na paǵina inicial se tentarem vir pela URL.

Página de criação de livro !
Existem: campo texto para titulo, botões para selecionar autor, categoria e capa. Campo texto para sinopse do livro e botão de enviar formulário para criar novo livro.
O adm pode criar livro no nome de quaisquer usuário.
O escritor pode criar livro no nome de quaisquer usuário por uma falha de segurança devida ao tempo para implementação.
Leitor/usuário não cadastrado: possuem acesso a essa página e podem criar no nome de qualquer autor porque não tivemos tempo suficiente para resolver isso.


Página de Login !
O cadastro está através do único link com underline na página; o login pode ocorrer através de 3 contas já criadas para sua experiência caso não deseje criar uma conta: 
Django Super user:
Login: rafaelrfeliciano
Senha: progamacaoWeb

Escritor:
Login: mirandawoops
Senha: mirandinhaF123

Leitor:
Login: pedrovillalobos
Senha: progweb2024


Pagina de Cadastro!
Existem 6 campos para inserção de texto: usuário, email, senha, confirmação de senha, primeiro nome e último nome. ALém disso, existe um select com os 3 grupos/cargos que existem no site. O cadastro não funciona. Existem 2 links no final da pagina: o primeiro para fazer login, redirecionando para página de login e outro para ver como leitor, redirecionando para home.


