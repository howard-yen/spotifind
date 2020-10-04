from nearby import *
from parse import *
from knn import *
from getinfo import *

def main(clients, clients_location):
    read_genres()
    update_db(clients, clients_location)
    nearby = get_nearby()
    similarity = knn()
    data = {}
    for userid, neighbors in similarity.items():
        data[userid] = []
        neighbor_ids = []
        neighbor_tokens = []
        for neighbor in neighbors:
            if neighbor in nearby[user]:
                neighbor_ids.append(neighbor)
                neighbor_tokens.append(clients[neighbor])

        data[userid] = get_neighbors_tracks(neighbor_tokens, neighbor_ids)

if __name__ == '__main__':
    locations = {
                "f948992952d94b4d90e39b81984ef9c3":
                    {"lat":37.5455744,"lon":-121.93628160000002},
                "f948992952d94b4d90e39b81984ef9c2":
                    {"lat":33.086937,"lon":-96.760109},
                "f948992952d94b4d90e39b81984ef9c1":
                    {"lat":37.5429949,"lon":-121.9318253},
                "f948992952d94b4d90e39b81984ef9c0":
                    {"lat":37.540140,"lon":-121.946590}
    }
    clients = {
        "f948992952d94b4d90e39b81984ef9c3":
        "BQDpyXP3XJECHi-sqSIqOkjNYwT-BinQ0y1I3mkn_jh0x28K2bEt5hB7RCp0CbUv012UVI5lKfBlSpChtCIezMMj7dErKS6bs2LEAJ7scUZZWJJzkvao-GvQ23pMc1NZk-oVe7OW4R4wFhyZjEMEaeRqKVUVHk5BfHVVcblqWxs",
        "f948992952d94b4d90e39b81984ef9c2":
        "BQDGy2yxYOLNybqmqfWu_fja1hvEL1rYhJUAhjvHdts6xgO1B3Q2ZI1ZVa4sd6dcHvATBDWbK4OBIhn4gUEfWohEI-kv9W0iKLiL6mp8tw0KKWmencE-yUJhaymtO_S5jg8I5xQvWUuX7UR4Fw_UTwAIvrbAcqbihhISbapH6aItVYdEsVmx6Zkqf2FmEXLY9XDkEPQNJomXuvw4AKWVrXMtRBSz_3kQV_FodmInfs3EzjtmDlAar1NtpTOt7W36wjeCKVEVGSkc",
        "f948992952d94b4d90e39b81984ef9c1":
        "BQAsYIHoE1FgwKoRFA7jmGWyn9KkVi60ZLMAsdsHnwkyPfDyYllL7DH3NdW4sl_BxD1C007SwDqAvwDCs7MlJsrRCWfmt4RvLMgya61e9lYYuHcErJwquomVksKMsJvURLi5hd7l0ZDGDanAjjsxfP6UslGnzAeQSbb9g4A_KjI",
        "f948992952d94b4d90e39b81984ef9c0":
        "BQAmpB7EsifUEGI6EE7LixioQ_p7BO6gBUETdwMM8hbjR1Z2JP5EPwOJ3gwuz0FvVE-fBD7bOPfqq2yJwfAzCTiPpMkwH2rADvOxe36dPjQy_S1CrbGnQFGjf8_g57m0f8J2uwQDaaaHb1eUxiQWwx2ej6D-V4Im6QO4CsiGaAs"
    }

    main(clients, locations)
