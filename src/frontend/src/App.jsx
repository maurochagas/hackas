import React, { useEffect, useState } from 'react';
import { getUsers, createUser } from './api/user_api';

const App = () => {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ username: '', email: '', full_name: '' });

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const usersData = await getUsers();
        setUsers(usersData);
      } catch (error) {
        console.error(error);
      }
    };

    fetchUsers();
  }, []);

  const handleCreateUser = async () => {
    try {
      const createdUser = await createUser(newUser);
      setUsers([...users, createdUser]);
      setNewUser({ username: '', email: '', full_name: '' });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Hackas</h1>
      <div>
        <h2 className="text-2xl font-semibold mb-2">Usuários</h2>
        <ul className="list-disc pl-5">
          {users.map((user) => (
            <li key={user.id} className="mb-1">{user.username}, {user.email}, {user.full_name}</li>
          ))}
        </ul>
      </div>
      <div className="mt-6">
        <h2 className="text-2xl font-semibold mb-2">Criar Usuário</h2>
        <div className="flex flex-col space-y-2">
          <input
            type="text"
            placeholder="Nome de usuário"
            value={newUser.username}
            onChange={(e) => setNewUser({ ...newUser, username: e.target.value })}
            className="p-2 border border-gray-300 rounded"
          />
          <input
            type="email"
            placeholder="Email"
            value={newUser.email}
            onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
            className="p-2 border border-gray-300 rounded"
          />
          <input
            type="text"
            placeholder="Nome completo"
            value={newUser.full_name}
            onChange={(e) => setNewUser({ ...newUser, full_name: e.target.value })}
            className="p-2 border border-gray-300 rounded"
          />
          <button
            onClick={handleCreateUser}
            className="bg-blue-500 text-white p-2 rounded hover:bg-blue-700"
          >
            Criar
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
