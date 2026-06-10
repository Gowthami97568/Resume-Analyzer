import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  // 📂 Select file
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // 🚀 Upload resume
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log(data); // Debug
      setResult(data);

    } catch (error) {
      console.error("Error:", error);
      alert("Backend not connected");
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>AI Resume Analyzer 🚀</h1>

      {/* File Upload */}
      <input type="file" onChange={handleFileChange} />
      <br /><br />

      <button onClick={handleUpload}>Upload Resume</button>

      {/* ✅ SAFE RESULT DISPLAY */}
      {result && result.all_skills && (
        <div style={{ marginTop: "20px" }}>

          <h2>Score: {result.score}</h2>

          <h3>Skills:</h3>
          <ul>
            {result.all_skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h3>Missing Skills:</h3>
          <ul>
            {result.missing_skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h3>Suggestions:</h3>
          <ul>
            {result.suggestions?.map((s, index) => (
              <li key={index}>{s}</li>
            ))}
          </ul>

        </div>
      )}
    </div>
  );
}

export default App;