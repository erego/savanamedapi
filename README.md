# savanamedapi
This is a medical technology searching API for healthcare professionals

# How to install
1. Clone de repo
2. Execute docker build -t savanamedapi . where the docker file is
3. Execute docker run -p 5010:5050 savanamedapi in order to run the API


# How to use

 To find  | Example of get use | Example of post use
| --------- | --------- | --------- 
| List of terms | curl http://localhost:5050/savanamedapi/get_terms?search=cirugia | curl  -H "Content-Type: application/json" -X POST -d '{"search":"embarazo"}' http://localhost:5010/savanamed/api/get_terms
| Detailed term | curl http://localhost:5050/savanamedapi/get_details?id=1 | curl  -H "Content-Type: application/json" -X POST -d '{"id":2}' http://localhost:5010/savanamed/api/get_details



