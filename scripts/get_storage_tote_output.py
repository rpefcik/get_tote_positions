import yaml

def extract_codes_from_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    def find_codes(obj):
        codes = []
        if isinstance(obj, dict):
            if obj.get("name") == "Empty_storage_tote":
                columns = obj.get("columns", [])
                for col in columns:
                    tote_positions = col.get("tote_positions", [])
                    for pos in tote_positions:
                        if "code" in pos:
                            codes.append(pos["code"])
            # Recurse into nested dicts
            for value in obj.values():
                codes.extend(find_codes(value))
        elif isinstance(obj, list):
            for item in obj:
                codes.extend(find_codes(item))
        return codes

    codes = find_codes(data)
    print("[ " + ", ".join(f'"{code}"' for code in codes) + " ]")

# Example usage
if __name__ == "__main__":
    extract_codes_from_yaml("../input_file.yaml")
