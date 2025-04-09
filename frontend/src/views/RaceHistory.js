import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RaceHistory = () => {
  const [races, setRaces] = useState([]);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem('user'));
    if (!user) {
      navigate('/');
      return;
    }

    fetch('http://localhost:5000/api/race-result', {
      method: 'GET',
      credentials: 'include',
    })
      .then((res) => {
        if (!res.ok) throw new Error('Not authorized or error loading data.');
        return res.json();
      })
      .then((data) => setRaces(data))
      .catch((err) => setError(err.message));
  }, [navigate]);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Race History</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {races.length === 0 ? (
        <p>No races found.</p>
      ) : (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>Event</th>
              <th>Location</th>
              <th>Date</th>
              <th>Result</th>
              <th>Place</th>
            </tr>
          </thead>
          <tbody>
            {races.map((race, index) => (
              <tr key={index}>
                <td>{race.event}</td>
                <td>{race.location}</td>
                <td>{new Date(race.date).toLocaleDateString()}</td>
                <td>{race.result}</td>
                <td>{race.place}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default RaceHistory;