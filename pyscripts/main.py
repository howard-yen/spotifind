from .nearby import *
from .parse import *
from .knn import *
from .getinfo import *

def main(clients, clients_location):
    clients = {'c882080090ff4a73951f135eb0103774': 'BQAGbREVB1538UmnbdOQ1abZu4-UAkh7nWUMmi10IojToytaQTzjFrva5Nz2M3zvBVWI8QGjcyl42XPg0dDtesv-E6QfbD5KiCVfp1ijQasPNHRc5UzSAG3vl8Y8wrVl77vWerRRel0iRObVr-wVtkBEtOW2c98Hg1Fp2w850gXvlbsQ'}
    read_genres()
    update_db(clients, clients_location)
    nearby = get_nearby()
    similarity = knn()
    data = {}
    for user in similarity:
        for i in user:
            if i in nearby[user]:
                data[user] = TOP_SONGS_JSON
