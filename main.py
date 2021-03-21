# T3 Distribuidos - Diego Iruretagoyena
# Simulación para validar y encontrar hashs,
# https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-4-task-queues/

import sys
from redis import Redis
from rq import Connection, Queue
from proof import generate_proof_of_work


PATH = sys.argv[1]
redis = Redis(host="localhost")
vip_queue = Queue('vipqueue', connection=redis)
alto_queue = Queue('altoqueue', connection=redis)
comun_queue = Queue('comunqueue', connection=redis)

with open("output.txt", "w") as file:
    pass

with open(PATH, "r") as instructions_file:
    for instruction in instructions_file.readlines():
        print(instruction)
        client_info = instruction.strip().split(" ")
        X_i = client_info[0]
        type_ = client_info[0][0]
        X_ID = client_info[1]
        last_k_ = client_info[2]
        end_string = client_info[3]
        if type_ == "V":
            job = vip_queue.enqueue_call(func=generate_proof_of_work,
                                           args=(int(last_k_), X_ID, end_string, X_i))
        if type_ == "T":
            job = alto_queue.enqueue_call(func=generate_proof_of_work,
                                          args=(int(last_k_), X_ID, end_string, X_i))
        if type_ == "C":
            job = comun_queue.enqueue_call(func=generate_proof_of_work,
                                           args=(int(last_k_), X_ID, end_string, X_i))
