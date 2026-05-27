import { useState } from "react";
import "./App.css";

function App() {

  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const explainQuery = async () => {

    setLoading(true);
    setResult("");

    try {

      const response = await fetch(
        "http://127.0.0.1:5000/explain",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            query: query,
          }),
        }
      );

      const data = await response.json();

      setResult(data.explanation);

    } catch (error) {

      setResult("Something went wrong.");

    }

    setLoading(false);
  };

  const copyResult = () => {

    navigator.clipboard.writeText(result);

    alert("Explanation copied!");
  };

  return (

    <div className="app">

      <div className="container">

        <h1>AI SQL Query Explainer</h1>

        <textarea
          placeholder="Paste your SQL query here..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

       <button onClick={explainQuery} disabled={loading}>

  {loading ? "Generating Explanation..." : "Explain Query"}

</button>
{loading && <div className="spinner"></div>}
        {result && (

          <div className="result-box">

            <div className="result-header">

              <h2>AI Explanation</h2>

              <button
                className="copy-btn"
                onClick={copyResult}
              >
                Copy
              </button>

            </div>

            <p>{result}</p>

          </div>
        )}

      </div>

    </div>
  );
}

export default App;