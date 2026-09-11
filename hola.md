# Este es un proyecto basicco que haremos con santi en dos semanas 
## Se trabajara con Fastapi , versel, railway y colocare los bash mas adelante justo ya


### Comandos para iniciar un entorno virtual 
 
``` bash
py -m venv venv  

```
### Comando que activara el entorno virtual 
``` bash
.\venv\Scripts\activate 

```

### Comando que instalara dependencias ( fastapi y slq y demas)
``` bash
pip install "fastapi[standard]" sqlalchemy pymysql
```


### Comando que refrescara y subira al entorno virtual las dependecias necesarias

``` bash
pip freeze > requirements.txt 
```
## Siempre que se instalen nuevas debemos ejecutar el comando
       
### Si le sale un error en aL Utilizar Fastapi, es Porque se esta selecionando un py que no es del entorno Virtual. SE busca el interprete en el entorno virtual 


``` bash
ctrl+shift+p
```
