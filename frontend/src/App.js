import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await fetch(
        "https://resume-analyzer-te2b.onrender.com/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setResult(data);

    } catch (error) {
      console.error(error);
      alert("Backend not connected");
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>AI Resume Analyzer 🚀</h1>

      <input type="file" onChange={handleFileChange} />
      <br /><br />

      <button onClick={handleUpload}>Upload Resume</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Score: {result.score}</h2>

          <h3>Skills:</h3>
          <ul>
            {result.all_skills?.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <h3>Missing Skills:</h3>
          <ul>
            {result.missing_skills?.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <h3>Suggestions:</h3>
          <ul>
            {result.suggestions?.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;