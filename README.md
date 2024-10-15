# EditoraDinamica
DOCKER: COMO USAR A IMAGEM GERADA, ENVIADA AO PROFESSOR ? 

sudo docker load -i imgDocker.tar     /* descarrega a imagem docker*/

sudo docker images                    /* queremos saber a imageID */

sudo docker run -d 175d45dcca62       /* essa foi a imgID exibida para mim, te cabe achar a imgID com repositório e tag, respectivamente, "django-docker:0.0.1" */ 

sudo docker run -d -p 8000:8000 175d45dcca62  /* isso mapeará o docker na porta 8080, caso não consiga acessar imediantamente por "127.0.0.1:8000" */
