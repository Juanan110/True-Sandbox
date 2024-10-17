import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [cats, setCats] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:80/cats') // Ajusta la URL según tu configuración
            .then(response => {
                setCats(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the cats!", error);
            });
    }, []);

    return (
        <div>
            <h1>Cat Cafe</h1>
            <h2>Cats</h2>
            <ul>
                {cats.map(cat => (
                    <li key={cat.id}>{cat.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;

