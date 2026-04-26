import copy

def generate_data():
    users = [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]
    return users

def replicate_data(users):
    assign_copy = users
    shallow = copy.copy(users)
    deep = copy.deepcopy(users)
    return assign_copy, shallow, deep

def modify_data(data, roll_no):
    for user in data:
        if roll_no % 2 == 0:
            user["data"]["files"].append("user646_file.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()
        user["data"]["usage"] += 100

def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap = set()

    for i in range(len(original)):
        orig_files = set(original[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if original[i]["data"]["files"] != deep[i]["data"]["files"]:
            leakage += 1
        else:
            safe += 1

        overlap = overlap.union(orig_files.intersection(deep_files))

    return leakage, safe, len(overlap)

def main():
    roll_no = 646

    original = generate_data()

    assign_copy, shallow, deep = replicate_data(original)

    print("\nBefore Modification:")
    print("Original:", original)

    modify_data(assign_copy, roll_no)
    modify_data(shallow, roll_no)

    print("\nAfter Modification:")
    print("Original:", original)
    print("Assignment Copy:", assign_copy)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)

    leakage, safe, overlap = check_integrity(original, shallow, deep)

    print("\nIntegrity Report:")
    print("Leakage Count:", leakage)
    print("Safe Count:", safe)
    print("Overlap Count:", overlap)

    print("\nResult Tuple:", (leakage, safe, overlap))

    print("\nExplanation:")
    print("Assignment and shallow copy affect original data due to shared references.")
    print("Deep copy remains independent and safe.")

    print("\nData Corruption Definition:")
    print("Data corruption occurs when original data changes unintentionally due to improper copying methods.")

main()
