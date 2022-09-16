from fastapi import FastAPI

#Querys:
q1 = 2021
q2 = "Hamilton"
q3 = "Autodromo Nazionale di Monza"
q4 = "Button"

description = """
F1_FastAPI helps you get Formula F1 race history.

## Queries:
    query1 -> Year with the most races.
    query2 -> Driver with the most first places.
    query3 -> Name of the most run circuit.
    query4 -> Driver with the highest number of points in total, whose constructor is of American or British nationality.

You can **download all data** in the following link:\n 
http://ergast.com/downloads/f1db_csv.zip

## Libraries used:

* **Pandas**.
* **Numpy**.
* **FastAPI**.
* **Uvicorn**.
"""

app = FastAPI(
    title = "F1_FastAPI ",
    description=description,
    version="0.0.1",
    contact={
        "name": "Cristhian Ipanaqué Sánchez",
        "url": "https://www.linkedin.com/in/cristhianipanaque/",
        "email": "cristhian.ipanaque@gmail.com",
    },
    license_info={
        "name": "GitHub - Cthed2",
        "url": "https://github.com/cthed2",
    },
)


@app.get("/")
def read_main():
    return "Single FastAPI Project"

@app.get("/query1")
def Year_with_the_most_races():
    return q1

@app.get("/query2")
def Driver_with_the_most_first_places():
    return q2

@app.get("/query3")
def Name_of_the_most_run_circuit():
    return q3

@app.get("/query4")
def Driver_with_the_highest_number_of_points_in_total_whose_constructor_is_of_American_or_British_nationality():
    return q4


