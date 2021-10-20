from py2neo import Graph, Node, Relationship, NodeMatcher
import json


graph = Graph("http://54.211.202.75:7474", auth=('neo4j', 'gasoline-neutron-candle'))


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
