import React from "react";
import Spline from "@splinetool/react-spline";

export default function App() {
  return (
    <div style={{ width: "100vw", height: "100vh", position: "relative" }}>
      {/* Spline Canvas */}
      <Spline scene="https://prod.spline.design/a9tHMuuzSctGoM9s/scene.splinecode" />

      {/* GitHub Link */}
      <a
        href="https://github.com/ayshyama"
        target="_blank"
        rel="noopener noreferrer"
        style={{
          position: "absolute",
          bottom: "20px",
          right: "20px",
          backgroundColor: "rgba(0, 0, 0, 1)",
          color: "#fff",
          padding: "10px 15px",
          borderRadius: "8px",
          textDecoration: "none",
          fontFamily: "Arial, sans-serif",
          fontSize: "14px",
          fontWeight: "bold",
          zIndex: 10,
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.3)",
        }}
      >
        github/igors.dev
      </a>
    </div>
  );
}
