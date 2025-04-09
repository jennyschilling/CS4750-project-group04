import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './views/Login';
import RaceHistory from './views/RaceHistory';
import AddRaceResult from './views/AddRaceResult';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/history" element={<RaceHistory />} />
        <Route path="/add-result" element={<AddRaceResult />} />
      </Routes>
    </Router>
  );
}

export default App;