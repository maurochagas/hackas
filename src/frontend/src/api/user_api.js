import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const user_api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const createUser = async (user) => {
    try {
        const response = await user_api.post('/users', user);
        return response.data;
    } catch (error) {
        throw new Error('Failed to create user');
    }
};

export const getUser = async (userId) => {
    try {
        const response = await user_api.get(`/users/${userId}`);
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch user');
    }
};

export const getUsers = async () => {
    try {
        const response = await user_api.get('/users');
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch users');
    }
};


export const updateUser = async (userId, user) => {
    try {
        const response = await user_api.put(`/users/${userId}`, user);
        return response.data;
    } catch (error) {
        throw new Error('Failed to update user');
    }
};

export const deleteUser = async (userId) => {
    try {
        const response = await user_api.delete(`/users/${userId}`);
        return response.data;
    } catch (error) {
        throw new Error('Failed to delete user');
    }
};