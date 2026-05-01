import React, { useState } from "react";
import Chat from "./Chat";
import Form from "./Form";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    doctor: "",
    interaction_type: "",
    date: "",
    time: "",
    attendees: "",
    topics: "",
    sentiment: "",
    notes: ""
  });

  return (
    <div className="app">
      <div className="header">AI CRM – HCP Module</div>

      <div className="layout">

        {/* LEFT BIG */}
        <div className="left">
          <Form formData={formData} setFormData={setFormData} />
        </div>

        {/* RIGHT SMALL */}
        <div className="right">
          <Chat setFormData={setFormData} />
        </div>

      </div>
    </div>
  );
}

export default App;