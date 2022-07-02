# touriGO
A tour and travel service aggregator platform for listing businesses writing blogs and exploring places ;). 

![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) 

## Getting Started
### Prerequisites

Make sure you have installed *visual studio c++*, *python3*, *pip package installer*, *pgadmin4* and *postgresql* before running the project.

### Installation

* Clone the repo
```git clone {repository link}```
   
* Open the migrations in home folder of the project and delete all the migration files which are numbered.
* Install postgresql and Pg-admin in your system.
* Create a database in pg admin.
* Update the database name and password in *settings.py* file of AMS folder to connect the database to our project.
* Change the directory to the place where manage.py file is available.
* Create a virtual environment
   * pip install virtualenv
   * virtualenv venv
   
* Work on the created environment

   * for cmd ```venv\Scripts\activate```
   
* Install the following pacakges using command prompt in the virtual environment
   
   * pip install -r requirements.txt
   
* Create django migrations for database using the following commands
   
   * python manage.py makemigrations
   * python manage.py sqlmigrate home 0001
   * python manage.py migrate
   
* Create a super user i.e, the admin
   
   python manage.py createsuperuser
   
   * The command prompt will ask for the username and password for the admin.
   * enter the required details
   
* Run the server and open the website at http://127.0.0.1:8000/ localhost
   
   python manage.py runserver
   
## Screenshots of the project running

![Blog Screenshot](https://user-images.githubusercontent.com/103559940/163727353-c4ed638f-5d94-4765-b7f5-c63a5e630a99.png)
![Restaurants](https://user-images.githubusercontent.com/103559940/163727368-c2cf5909-5d54-4594-b348-82f2badb1b75.png)
![Tour](https://user-images.githubusercontent.com/103559940/163727376-51a20468-6dc5-4fff-a0c4-054be37236af.png)
![Travel](https://user-images.githubusercontent.com/103559940/163727391-d81331c0-50e5-4c19-8ab3-46172bb72bc7.png)



## Flowhart
![image](https://user-images.githubusercontent.com/103559940/163727471-b4c3e9b0-a03e-4fdc-a4c1-9aa734d78a26.png)

## Use Case Diagram
- Login:
![image](https://user-images.githubusercontent.com/103559940/163727487-9922c5b2-a013-4491-8385-b3082efc0aae.png)

- Service Users:
![image](https://user-images.githubusercontent.com/103559940/163727503-f40834f1-4c0b-432c-8718-4ac9eabe2af8.png)

- Service Providers:
![image](https://user-images.githubusercontent.com/103559940/163727532-929058b9-4d5c-4f06-aba2-8bc557f99b98.png)


## Class Diagram
![image](https://user-images.githubusercontent.com/103559940/163727549-6e6fe6c0-667c-4871-8b21-e6d3db7e0987.png)

## Sequence Diagrams
![image](https://user-images.githubusercontent.com/103559940/163727564-3991a6c3-4722-4a1a-bcd2-f4ebaae03d4e.png)

## Contributours Details
   * [Ujjwal Kumar Dubey](https://github.com/Kukudu-Koo)
   * [Prabhav Rohilla](https://github.com/PrabhavRohilla)
   * [Arpeit Chourasiya](https://github.com/Arpeit08)
   * [Devesh Kumar](https://github.com/kumar-devesh)
   * [Raunak Kumar](https://github.com/Raunak6402)
   * [Aleena M R](https://github.com/Aleena712)
