import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function Chat({ setFormData }) {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const send = async () => {
    if (!msg.trim()) return;

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        { input_text: msg }
      );

      const aiData = res.data;

      // ✅ show readable response instead of raw JSON
      const botMessage = aiData.action === "edit"
        ? `Updated ${aiData.field} → ${aiData.value}`
        : `Doctor: ${aiData.doctor_name || "-"}, Sentiment: ${aiData.sentiment || "-"}`;

      setChat(prev => [
        ...prev,
        { user: msg, bot: botMessage }
      ]);

      // 🔥 HANDLE LOG (auto-fill multiple fields safely)
      if (aiData.action === "log") {
        setFormData(prev => ({
          ...prev,
          doctor: aiData.doctor_name || prev.doctor,
          interaction_type: aiData.interaction_type || prev.interaction_type,
          date: aiData.date || prev.date,
          time: aiData.time || prev.time,
          attendees: aiData.attendees || prev.attendees,
          topics: aiData.topics || prev.topics,
          sentiment: aiData.sentiment || prev.sentiment,
          notes: aiData.summary || prev.notes
        }));
      }

      // 🔥 HANDLE EDIT (update only ONE field)
      if (aiData.action === "edit") {
        setFormData(prev => ({
          ...prev,
          [aiData.field]: aiData.value
        }));
      }

      setMsg("");
    } catch (err) {
      console.error(err);
      alert("Backend not connected");
    }
  };

  return (
    <div className="chat-container">
      <h3>🤖 AI Assistant</h3>

      <div className="chat-box">
        {chat.map((c, i) => (
          <div key={i}>
            <div className="user-msg">{c.user}</div>
            <div className="bot-msg">{c.bot}</div>
          </div>
        ))}
      </div>

      <div className="chat-input">
        <input
          value={msg}
          onChange={(e) => setMsg(e.target.value)}
          placeholder="Type interaction or correction..."
        />
        <button onClick={send}>Send</button>
      </div>
    </div>
  );
}

export default Chat;