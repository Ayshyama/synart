import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import Spline from "@splinetool/react-spline";

function GitHubLink({ zoom }) {
  return ReactDOM.createPortal(
    <div
      style={{
        position: "fixed",
        bottom: "28px",
        right: "18px",
        zIndex: 10000,
        pointerEvents: "auto",
        transform: zoom ? "scale(1.05)" : "scale(1)",
        transition: "transform 0.2s ease-in-out",
      }}
    >
      <a
        href="https://github.com/ayshyama"
        target="_blank"
        rel="noopener noreferrer"
        style={{
          backgroundColor: "rgba(0, 0, 0, 1)",
          color: "#fff",
          padding: "12px 16px",
          borderRadius: "8px",
          textDecoration: "none",
          fontFamily: "Arial, sans-serif",
          fontSize: "15px",
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.3)",
        }}
      >
        github/igors.dev
      </a>
    </div>,
    document.body
  );
}

export default function App() {
  const containerRef = useRef(null);
  const [isZoomed, setIsZoomed] = React.useState(false);

  useEffect(() => {
    // Отключаем выделение текста
    document.body.style.userSelect = "none";
    document.body.style.webkitUserSelect = "none";
    document.body.style.msUserSelect = "none";
    document.body.style.MozUserSelect = "none";

    return () => {
      document.body.style.userSelect = "";
      document.body.style.webkitUserSelect = "";
      document.body.style.msUserSelect = "";
      document.body.style.MozUserSelect = "";
    };
  }, []);

  const handleTouch = () => {
    // Вибрация
    if (navigator.vibrate) {
      navigator.vibrate(50);
    }

    // Анимация зума
    setIsZoomed(true);
    setTimeout(() => setIsZoomed(false), 200);
  };

  return (
    <div
      ref={containerRef}
      onTouchStart={handleTouch}
      style={{
        width: "100vw",
        height: "100vh",
        position: "relative",
        overflow: "hidden",
        touchAction: "manipulation", // Оптимизация работы тач-событий
      }}
    >
      {/* Spline Canvas */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          transform: isZoomed ? "scale(1.05)" : "scale(1)",
          transition: "transform 0.2s ease-in-out",
          zIndex: 0,
        }}
      >
        <Spline scene="https://prod.spline.design/a9tHMuuzSctGoM9s/scene.splinecode" />
      </div>

      {/* Telegram Login Widget */}
      <div
        id="telegram-login-widget"
        style={{
          position: "absolute",
          bottom: "70px",
          right: "20px",
          zIndex: 10,
        }}
      >
        <script
          async
          src="https://telegram.org/js/telegram-widget.js?8"
          data-telegram-login="synart_bot"
          data-size="large"
          data-radius="10"
          data-auth-url="https://igors.dev/auth/telegram"
          data-request-access="write"
        ></script>
      </div>

      {/* GitHub Link */}
      <GitHubLink zoom={isZoomed} />
    </div>
  );
}
