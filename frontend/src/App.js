import React, { useState } from "react";
import "./App.css";
import StudentRegistration from "./StudentRegistration"; // Componente de registro para estudiantes
import TeacherRegistration from "./TeacherRegistration"; // 

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Estado para login
  const [classes, setClasses] = useState([
    { id: 1, name: "Base de datos", group: "Grupo A", code: "12734" },
  ]); // Lista de clases
  const [showAddClassForm, setShowAddClassForm] = useState(false); // Estado para mostrar/ocultar modal
  const [newClass, setNewClass] = useState({ name: "", group: "", code: "" }); // Datos de nueva clase
  const [view, setView] = useState("login"); // Estado para manejar vistas (login, registro)

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewClass({ ...newClass, [name]: value });
  };

  const handleAddClass = (e) => {
    e.preventDefault();
    if (!newClass.name || !newClass.group || !newClass.code) {
      alert("Por favor completa todos los campos.");
      return;
    }
    setClasses([...classes, { ...newClass, id: Date.now() }]);
    setShowAddClassForm(false);
    setNewClass({ name: "", group: "", code: "" });
  };

  const renderLogin = () => (
    <div className="login-container">
      <div className="logo">
        <h1>Attenzio</h1>
      </div>
      <form className="login-form">
        <input type="email" placeholder="Correo electrónico" />
        <input type="password" placeholder="Contraseña" />
        <button
          type="button"
          onClick={() => setIsLoggedIn(true)} // Simula inicio de sesión
        >
          Iniciar Sesión
        </button>
      </form>
      <div className="register-link">
        <p>
          ¿No tienes cuenta?{" "}
          <a
            href="#"
            onClick={() => setView("selectRegister")} // Cambia a la vista de selección de registro
          >
            Regístrate aquí
          </a>
        </p>
      </div>
    </div>
  );

  const renderProfesor = () => (
    <div className="profesor-container">
      <div className="sidebar">
        <ul>
          <li>Home</li>
          <li>Configuración</li>
          <li>Reportes</li>
          <li onClick={() => setIsLoggedIn(false)}>Cerrar sesión</li>
        </ul>
      </div>
      <div className="main-content">
        <h1>Hola, ¿Qué deseas hacer?</h1>
        <div className="tarjetas-clases">
          {classes.map((clase) => (
            <div key={clase.id} className="tarjeta-clase">
              <h2>{clase.name}</h2>
              <p>{clase.group}</p>
              <p>{clase.code}</p>
            </div>
          ))}
          <div
            className="tarjeta-clase agregar-clase"
            onClick={() => setShowAddClassForm(true)}
          >
            <span>+</span>
            <p>Añadir otra clase</p>
          </div>
        </div>
      </div>

      {showAddClassForm && (
        <div className="modal">
          <h2>Añadir Clase</h2>
          <form onSubmit={handleAddClass}>
            <input
              name="name"
              type="text"
              placeholder="Nombre de la clase"
              value={newClass.name}
              onChange={handleInputChange}
            />
            <input
              name="group"
              type="text"
              placeholder="Grupo"
              value={newClass.group}
              onChange={handleInputChange}
            />
            <input
              name="code"
              type="text"
              placeholder="Código"
              value={newClass.code}
              onChange={handleInputChange}
            />
            <button type="submit">Añadir</button>
          </form>
          <button onClick={() => setShowAddClassForm(false)}>Cerrar</button>
        </div>
      )}
    </div>
  );

  const renderSelectRegister = () => (
    <div className="register-container">
      <h1>Registro de Usuarios</h1>
      <p>Selecciona el tipo de usuario que deseas registrar:</p>
      <div className="user-type">
        <button onClick={() => setView("studentRegister")}>Estudiante</button>
        <button onClick={() => setView("teacherRegister")}>Profesor</button>
      </div>
    </div>
  );

  return (
    <div className="App">
      {view === "login" && renderLogin()}
      {view === "selectRegister" && renderSelectRegister()}
      {view === "studentRegister" && <StudentRegistration />}
      {view === "teacherRegister" && <TeacherRegistration />}
      {isLoggedIn && renderProfesor()}
    </div>
  );
}

export default App;

