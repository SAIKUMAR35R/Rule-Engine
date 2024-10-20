from fastapi import FastAPI, HTTPException # type: ignore
from pymongo import MongoClient # type: ignore
from rule_engine import create_rule, combine_rules, evaluate_rule

app = FastAPI()

# MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['rule_engine_db']
rules_collection = db['rules']

@app.post("/create_rule")
async def create_rule_endpoint(rule_string: str):
    ast = create_rule(rule_string)
    rules_collection.insert_one({"rule_string": rule_string, "ast": ast})
    return {"message": "Rule created successfully", "ast": ast}

@app.post("/combine_rules")
async def combine_rules_endpoint(rule_ids: list):
    rules = [rule["rule_string"] for rule in rules_collection.find({"_id": {"$in": rule_ids}})]
    combined_ast = combine_rules(rules)
    return {"combined_ast": combined_ast}

@app.post("/evaluate_rule")
async def evaluate_rule_endpoint(data: dict, rule_id: str):
    rule = rules_collection.find_one({"_id": rule_id})
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    result = evaluate_rule(rule["ast"], data)
    return {"result": result}
