import yaml
import argparse

def extract_codes_from_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    def find_codes(obj):
        codes = []
        if isinstance(obj, dict):
            if obj.get("name") == "Decanting":
                columns = obj.get("columns", [])
                for col in columns:
                    tote_positions = col.get("tote_positions", [])
                    for pos in tote_positions:
                        if "code" in pos:
                            codes.append(pos["code"])
            for value in obj.values():
                codes.extend(find_codes(value))
        elif isinstance(obj, list):
            for item in obj:
                codes.extend(find_codes(item))
        return codes

    codes = find_codes(data)
    print("[ " + ", ".join(f'"{code}"' for code in codes) + " ]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract position codes from a YAML file.")
    parser.add_argument("filepath", help="Path to the YAML file to parse")
    args = parser.parse_args()

    extract_codes_from_yaml(args.filepath)
