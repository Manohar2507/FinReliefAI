function App() {
  return (
    <div
      style={{
        textAlign: "center",
        padding: "60px",
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f4f4f4",
        minHeight: "100vh",
      }}
    >
      <h1>💰 FinRelief AI</h1>

      <h2>AI Powered Debt and Financial Recovery Platform</h2>

      <p style={{ fontSize: "18px", marginTop: "20px" }}>
        Welcome to the FinRelief AI Frontend.
      </p>

      <p>
        This frontend is built using <b>React.js</b> and <b>Vite</b>.
      </p>

      <button
        style={{
          padding: "12px 25px",
          fontSize: "18px",
          backgroundColor: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          marginTop: "20px",
        }}
      >
        Get Started
      </button>

      <hr style={{ margin: "40px" }} />

      <h3>Project Features</h3>

      <ul
        style={{
          display: "inline-block",
          textAlign: "left",
          fontSize: "18px",
        }}
      >
        <li>Python Flask Backend</li>
        <li>React + Vite Frontend</li>
        <li>REST API Integration</li>
        <li>AI Powered Financial Assistance</li>
        <li>Modern Responsive Interface</li>
      </ul>
    </div>
  );
}

export default App;