import { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: prompt })
    };

    const apiResponse = await fetch('http://localhost:5000/api/generate-response', requestOptions);
    const data = await apiResponse.json();

    setResponse(data.response);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          Prompt:
          <input type="text" value={prompt} onChange={handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <div>{response}</div>
    </div>
  );
}

export default App;
