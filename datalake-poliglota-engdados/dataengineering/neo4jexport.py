from py2neo import Graph, Node, Relationship, NodeMatcher
import json


graph = Graph("url", auth=('user', 'password'))


def export():
    query = '''
            MATCH p=()-->() RETURN p
            '''

    posts = graph.run(query).data()

    with open('miniblog_neo4j.json', 'w') as file:
        file.write('[')
        for post in posts:
            file.write(str(post))
            file.write(',')
        file.write(']')


if __name__ == "__main__":
    export()
