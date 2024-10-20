import React, { useState } from "react";
import axios from "axios";

function App() {
  const [rule, setRule] = useState("");
  const [data, setData] = useState({});
  const [result, setResult] = useState(null);

  const createRule = async () => {
    const response = await axios.post("/create_rule", { rule_string: rule });
    console.log(response.data);
  };

  const evaluateRule = async () => {
    const response = await axios.post("/evaluate_rule", { data: data, rule_id: "rule_id_here" });
    setResult(response.data.result);
  };

  return (
    <div>
      <h1>Rule Engine</h1>
      <input type="text" value={rule} onChange={(e) => setRule(e.target.value)} />
      <button onClick={createRule}>Create Rule</button>

      <h2>Evaluate Rule</h2>
      <input type="text" placeholder="age" onChange={(e) => setData({ ...data, age: e.target.value })} />
      <input type="text" placeholder="salary" onChange={(e) => setData({ ...data, salary: e.target.value })} />
      <button onClick={evaluateRule}>Evaluate</button>

      {result !== null && <h3>Result: {result ? "True" : "False"}</h3>}
    </div>
  );
}

export default App;
