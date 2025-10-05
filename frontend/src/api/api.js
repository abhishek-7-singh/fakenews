export const fetchNews = async () => {
    const response = await fetch("http://127.0.0.1:5000/get_news");
    return response.json();
};

export const checkFakeNews = async (text) => {
    const response = await fetch("http://127.0.0.1:5000/check_news", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
    });
    return response.json();
};

export const matchNews = async (text) => {
    const response = await fetch("http://127.0.0.1:5000/match_news", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
    });
    return response.json();
};
