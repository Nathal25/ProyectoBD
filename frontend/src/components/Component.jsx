import React, { useState } from 'react';

function Login() {
  const [userType, setUserType] = useState('Estudiante');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email || !password) {
      alert('Por favor completa todos los campos');
      return;
    }
    console.log(`Usuario: ${userType}, Correo: ${email}`);
  };

  return (
    <div className="login-container">
      <h1>Attenzio</h1>
      <div className="user-type">
        <button
          className={userType === 'Estudiante' ? 'active' : ''}
          onClick={() => setUserType('Estudiante')}
        >
          Estudiante
        </button>
        <button
          className={userType === 'Profesor' ? 'active' : ''}
          onClick={() => setUserType('Profesor')}
        >
          Profesor
        </button>
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Correo institucional"
          required
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Contraseña"
          required
        />
        <button type="submit">Iniciar sesión</button>
      </form>
      <p className="register-link">
        {userType === 'Estudiante'
          ? '¿No estás registrado? '
          : '¿Eres profesor nuevo? '}
        <a href="#">Regístrate aquí</a>
      </p>
    </div>
  );
}

export default Login;