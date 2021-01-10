# import the neo4j driver for Python

from neo4j import GraphDatabase

# Database Credentials

uri             = "bolt://localhost:7687"

userName        = "neo4j"

password        = "8hY&BZZaa@#!"

# Connect to the neo4j database server

graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password))

cqlCreate = """CREATE (SIonovIt:user_info { username: "SIonovIt", password: "BadPassword", favorite_weather: "Mild", zip: "19320"}),

(OnTIoNct:user_info { username: "OnTIoNct", password: "NonHashed", favorite_weather: "Cold", zip: "61821"}),

(aNTAGNaR:user_info { username: "aNTAGNaR", password: "Reversible", favorite_weather: "Sunny", zip: "22180"}),

(BrAhEral:user_info { username: "BrAhEral", password: "Plaintext", favorite_weather: "Cloudy", zip: "34711"}),

(IDefaRyp:user_info { username: "IDefaRyp", password: "simple", favorite_weather: "Snowing", zip: "07450"}),

(ETHEmenT:user_info { username: "ETHEmenT", password: "Blue", favorite_weather: "Raining", zip: "19111"}),

(TSetSCEr:user_info { username: "TSetSCEr", password: "Orange", favorite_weather: "Overcast", zip: "42431"}),

(AbERYLSA:user_info { username: "AbERYLSA", password: "Yellow", favorite_weather: "Windy", zip: "83651"}),

(UmeNTati:user_info { username: "UmeNTati", password: "Green", favorite_weather: "Hot", zip: "24073"}),

(CaTOneRf:user_info { username: "CaTOneRf", password: "Red", favorite_weather: "Sunny", zip: "90278"})

"""

# Execute the CQL query

with graphDB_Driver.session() as graphDB_Session:

    # Create nodes

    graphDB_Session.run(cqlCreate)

