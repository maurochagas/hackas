import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const gemini_api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const generateText = async (prompt) => {
    try {
        const response = await gemini_api.post('/gemini/generate', { prompt });
        return response.data.response;
    } catch (error) {
        throw new Error('Failed to generate text');
    }
};