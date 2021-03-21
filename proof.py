import hashlib


def validate_proof_of_work(last_k, last_hash, k, end_hash):
    sha = hashlib.sha256(f"{last_k}{last_hash}{k}".encode())
    return sha.hexdigest()[:len(end_hash)] == end_hash


def generate_proof_of_work(last_k, last_hash, end_hash, client):
    k=0
    while not validate_proof_of_work(last_k, last_hash, k, end_hash):
        k += 1
    with open("output.txt", "a") as result:
        result.write("Tipo: " + client + "| k_prima: " + str(k) + "| last_hash: " + str(last_hash) + "| last_hash: " + str(end_hash)+"\n")
    return k

