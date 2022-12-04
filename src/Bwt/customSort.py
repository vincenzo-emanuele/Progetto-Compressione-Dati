import random

def getSecretSort(alfabeto, key):
    # Estraggo l'alfabeto e randomizzo il mapping dei caratteri
	remap_dict = dict()
	random.seed(key)
	for i in alfabeto:
		remap_dict[i] = random.random()
	
	# Impongo che l'EOF sia minore in ordine lessicografico
	remap_dict["\003"] = -1
	return remap_dict


if __name__ == "__main__":

    input = "Destiny is mine"
    alfabeto = sorted(set(input))
    random.seed("asdf")
    remap_dict = dict()
    random_array = []
    for i in range(0, len(alfabeto)):
        random_array.append(random.random())

    print("Random array: " + str(random_array))
    for i in range(0, len(alfabeto)):
        remap_dict[alfabeto[i]] = random_array[i]

    print(dict(sorted(remap_dict.items(), key=lambda item: item[1])))
    
    # Prendiamo il dizionario dalla stringa input
    # Creiamo un array di len(stringa) numeri random (già con il seed)
    # dict che assegna ad ogni carattere dell'alfabeto il suo valore random
    # 