import socket
import json
import mysql.connector
import settings



with open("domains.txt") as input_file:
    domains = input_file.read().split()

    result = []
    for domain in domains:
        ip = socket.gethostbyname(domain)
            
        result.append({
            "name": domain,
            "ip": ip
        })

with open("domains.json", "w") as output_file:
    result_json = json.dumps(result, indent=4)
    output_file.write(result_json)
    
connection = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    port=settings.port,
    # database=settings.db_name
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Internet")
cursor.execute("USE Internet")
cursor.execute("CREATE TABLE IF NOT EXISTS Domain (id INT AUTO_INCREMENT PRIMARY KEY, domain VARCHAR(255) NOT NULL, ip VARCHAR(45) NOT NULL)")

for i in result:
    cursor.execute("INSERT INTO Domain (domain, ip) VALUES (%s, %s)", (i["name"], i["ip"]))
    
connection.commit()
connection.close()
    

            


