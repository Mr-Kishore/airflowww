***Hello everyone!***<br>
    I know, new repository new thing that means new thing to stress about....! 😅😅
    It's it confusing but never low on fun so we can do it, We are gonna study about airflow !!!

**AIRFLOW?? you mean the flow of air?**,<br>
		Yes and no, confusing right? it is the flow but not for the air but for the air but for the tasks or programs.
	It plays a major role in programmes like Data Engineering, Data Science and feilds related to data processings etc<br>
		It is used to monitor the flow of a process (one liner you can always check the resouce page)<br><br>
				                            https://airflow.apache.org/ <br> <br>
																
**INSTALLTION**<br>
		Yes, its the time of installation folks. First let's see the required materials

		Visual Studio Code(I personally use this so...)
		Docker
		Python (3.10 is more stable)
		knowledge about .yaml file formats
		and finally a .env file 


I have pasted my files here so you guys can check it.<br> <br>
 **what does these do???** <br>

	1. *Visual Studio Code* of course, to code. <br>
 	2. *Docker* to host the **Airflow UI**. <br>
 	3. *Python* don't act like you don't know what to do with that. <br>
 	4. *.yaml file* because it tells Docker how to set up and run your Airflow environment using Docker-Compose. <br>
 	5. *.env file* for creating the environment. <br>
	6. in the terminal dont forget to install airflow
 				pip install apache-airflow
these are the igredients that we are gonna cook (or get cooked. who knows.....)  <br> <br>

1. Create a new folder and open it <br>
2. create the .yaml file <br>
3. create the .env file <br>
4. make sure doker is running in the background <br>
5. if you're sure that you did all tings right run it with the command <br>

   				docker-compose up --build
6.You will see the airflow UI running <br>


some important commands <br>

		docker-compose down --volumes --remove-orphans   (removes existing running airflow operations (like clear cache))
		docker-compose up airflow-init     (initializes airflow)
		docker-compose up --build  (runs the airflow UI)


	
