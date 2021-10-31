import json
genome = "./genome.csv"

dict_genome = {}

with open(genome, "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        key, value = line.split(",")
        
        if i == 0:
            dict_genome['headers'] = [key, value]
        else:
            if key not in dict_genome:
                dict_genome[key] = [value]
            else:
                dict_genome[key].append(value)
        
    print(json.dumps(dict_genome, sort_keys=True, indent=2))