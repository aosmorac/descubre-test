# descubre-test

You can run it into the docker in this git or in your own machine.

## Clone this git

```
git clone https://github.com/aosmorac/descubre-test.git
```

## Running Docker

Go into the project folder
```
cd descubre-test
```

Run docker
```
docker-compose up
```

Go into docker container, using a different terminal
```
docker exec -i -t python-first bash
```


If you want to run this code in your machine just go to code/ folder


## Sample Session

GetCategories API to download the category tree and create the SQLite database

```
./categories --rebuild
```

Or you can use

```
./rebuild
```

output a file html that contains a simple web page displaying the sub categories list 

```
./categories --render 183627 
ls 183627.html
183627.html
```
```
./categories --render 6666666666 
No category with ID: 6666666666
```

Or you can use

```
./render 183627 
ls 183627.html
183627.html
```
```
./render 6666666666 
No category with ID: 6666666666
```



