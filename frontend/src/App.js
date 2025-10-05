import React, { useState, useEffect } from "react";
import { fetchNews, checkFakeNews, matchNews } from "./api/api";

function App() {
    const [news, setNews] = useState([]);
    const [inputText, setInputText] = useState("");
    const [fakeResult, setFakeResult] = useState(null);
    const [matchResult, setMatchResult] = useState(null);

    useEffect(() => {
        fetchNews().then(setNews);
    }, []);

    const handleCheckNews = async () => {
        const result = await checkFakeNews(inputText);
        setFakeResult(result);
    };

    const handleMatchNews = async () => {
        const result = await matchNews(inputText);
        setMatchResult(result);
    };

    return (
        <div>
            <h1>Fake News Detection</h1>
            <input
                type="text"
                placeholder="Enter news text..."
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
            />
            <button onClick={handleCheckNews}>Check Fake News</button>
            <button onClick={handleMatchNews}>Match News</button>

            {fakeResult && <p>Fake News: {fakeResult.is_fake ? "Yes" : "No"}</p>}
            {matchResult && <p>Match Score: {matchResult.match_score.toFixed(2)}</p>}

            <h2>Latest News</h2>
            <ul>
                {news.map((article, index) => (
                    <li key={index}>{article.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
