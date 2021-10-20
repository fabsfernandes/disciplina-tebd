from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient("mongodb+srv://dbUser:dbUserPassword@sandbox.pdrwt.mongodb.net/test?retryWrites=true&w=majority")
db = client.tododb
todos = db.todo


def export():
    todos_all = todos.find()

    with open('tarefastodo_mongodb.json', 'w') as file:
        file.write('[')
        num_max = todos.count_documents({})
        cont = 0
        for document in todos_all:
            file.write(dumps(document))
            cont+=1
            if cont < num_max:
                file.write(',')
        file.write(']')


if __name__ == "__main__":
    export()
