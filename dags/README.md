**DAGs...!**<br>
    The **D**irected **A**cyclic **G**raphs or (Dags)  is a collection of all the tasks you want to run,
organized in a way that reflects their relationships and dependencies.<br>
    In this project the Dags are being run in python 🐍

*To check the working of the dag*<br>
    once the dag is saved you have to close and run the *Airflow UI* again, for this you have to type 
the command 

            docker-compose down --volumes --remove-orphans  #used to clear all cache files
            docker-compose up --build   #used to start the airflow ui again

after this you should be able to see your dag in the airflow ui<br>
![image](https://github.com/user-attachments/assets/41894eaa-2cfb-488d-9c4d-822360b70d75) <br>

*How to run the dag??* <br>
        To run the dag first you have to select the dag<br>
        ![image](https://github.com/user-attachments/assets/da62bee9-1af7-4dd9-a866-b93ef8f1d1be)<br>
        then click the trigger button <br>
        ![image](https://github.com/user-attachments/assets/ed2e704e-26d6-4cdf-ad83-2519cb74da5e)<br>
        you'll see the dag running and completion<br>
        ![image](https://github.com/user-attachments/assets/f6246fb1-a5d3-41b4-b110-b59ee2a2663d) <br>
        to see the workflow use the graph tab<br>
        ![image](https://github.com/user-attachments/assets/4650a52e-1051-43a5-914d-5458417b5675)
        then to see the output view the logs tab<br>
        ![image](https://github.com/user-attachments/assets/0e4f237d-fe71-4f34-ab68-7318e2d2bdf0) <br>

If this happens in your first attempt (idk what to tell you're a genius) <br>
if you get into more troubles feel free to contact kishoreprogramminghub@gmail.com .






