# Rule Engine with AST

## Objective
Develop a simple 3-tier rule engine application (UI, API, and Backend) to determine user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Data Structure
- **Node**: Represents the AST.
  - `type`: String indicating the node type ("operator" for AND/OR, "operand" for conditions)
  - `left`: Reference to another Node (left child)
  - `right`: Reference to another Node (right child for operators)
  - `value`: Optional value for operand nodes (e.g., number for comparisons)

## Data Storage
- **Database**: [Define your choice of database, e.g., SQLite, PostgreSQL, etc.]
- **Schema**: 
  - `rules` table:
    - `id`: Primary Key
    - `rule_string`: Text
    - `created_at`: Timestamp

### Sample Rules
- `rule1`: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
- `rule2`: "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

## API Design
1. `create_rule(rule_string)`: Returns a Node object representing the corresponding AST.
2. `combine_rules(rules)`: Combines a list of rule strings into a single AST, minimizing redundant checks.
3. `evaluate_rule(data)`: Evaluates the rule against provided data and returns True or False.

## Test Cases
1. Create individual rules using `create_rule` and verify their AST representation.
2. Combine example rules using `combine_rules` and validate the resulting AST.
3. Implement sample JSON data and test `evaluate_rule` for various scenarios.
4. Explore combining additional rules and test the functionality.

## Bonus Features
- Error handling for invalid rule strings or data formats.
- Validation for attributes in a catalog.
- Modification of existing rules with additional functionalities.
- Support for user-defined functions within the rule language.

## Installation
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
