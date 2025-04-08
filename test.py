import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open('test.json') as t:
    doc = json.load(t)

with open('test-schema.json') as f: 
    schema = json.load(f)

try:
    validate(instance=doc, schema=schema)
    print("Validation succeeded!")
except ValidationError as e:
    print("Validation failed!")
    print(f"Error msg:{e.message}")