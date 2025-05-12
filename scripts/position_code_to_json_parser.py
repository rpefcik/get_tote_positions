import yaml
import json

with open("warehouse.yaml", "r") as file:
    data = yaml.safe_load(file)

try:
    inputs = data.get('storage_tote_inputs')
    if not inputs or not isinstance(inputs, list):
        raise ValueError("Missing or invalid 'storage_tote_inputs' list")

    tote_codes = []
    starting_tote_code = 222000001

    for input_entry in inputs:
        columns = input_entry.get('columns', [])
        if not isinstance(columns, list):
            continue

        for column in columns:
            positions = column.get('tote_positions')

            if isinstance(positions, list):
                for pos in positions:
                    code = pos.get('code')
                    if code:
                        tote_entry = {"position_code": code, "tote_code": str(starting_tote_code)}
                        tote_codes.append(tote_entry)
                        starting_tote_code += 1 # plus 1 tote code

    if not tote_codes:
        raise ValueError("No tote codes found.")

    with open("../output.json", "w") as out_file:
        json.dump(tote_codes, out_file, indent=2)

    print("✅ Extracted and saved JSON list")

except Exception as e:
    print("❌ Error:", e)
