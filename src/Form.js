import React from "react";
import "./App.css";

function Form({ formData, setFormData }) {
  return (
    <div className="form-container">
      <h2>Interaction Details</h2>

      <input value={formData.doctor} placeholder="HCP Name"
        onChange={(e)=>setFormData({...formData, doctor:e.target.value})} />

      <select value={formData.interaction_type}
        onChange={(e)=>setFormData({...formData, interaction_type:e.target.value})}>
        <option value="">Interaction Type</option>
        <option>Visit</option>
        <option>Call</option>
        <option>Meeting</option>
      </select>

      <input type="date" value={formData.date}
        onChange={(e)=>setFormData({...formData, date:e.target.value})} />

      <input type="time" value={formData.time}
        onChange={(e)=>setFormData({...formData, time:e.target.value})} />

      <input value={formData.attendees} placeholder="Attendees"
        onChange={(e)=>setFormData({...formData, attendees:e.target.value})} />

      <textarea value={formData.topics} placeholder="Topics Discussed"
        onChange={(e)=>setFormData({...formData, topics:e.target.value})} />

      <select value={formData.sentiment}
        onChange={(e)=>setFormData({...formData, sentiment:e.target.value})}>
        <option value="">HCP Sentiment</option>
        <option>Positive</option>
        <option>Neutral</option>
        <option>Negative</option>
      </select>

      <textarea value={formData.notes} placeholder="Notes"
        onChange={(e)=>setFormData({...formData, notes:e.target.value})} />

      <button>Save</button>
    </div>
  );
}

export default Form;