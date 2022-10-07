from fastapi import FastAPI

app = FastAPI()

response = {
    1 : {
        'name' : 'Aryan',
        'age' : 16
    },
    2 : {
        'name' : 'Elon',
        'age' : 50
    }
}

@app.get('/get-user/{id}')
def getUser(id: int):
    return response[id]

@app.get('/all-users')
def allUsers():
    return response

@app.post('/create-user')
def createUser(name: str, age: int):
    finalKey = list(response.keys())

    temp = {
        'name' : name,
        'age' : age
    }
    
    response[finalKey[len(finalKey) - 1]] = temp

    return response

@app.put('/update-user/{id}')
def updateUser(id: int, name: str, age: int):
    response[id] = {
        'name' : name,
        'age' : age,
    }

    return response

