import React, { useState } from "react";

const TeacherRegistration = () => {
  const [formData, setFormData] = useState({
    nombres: "",
    apellidos: "",
    correoInstitucional: "",
    numeroCelular: "",
    materia: "",
  });

  const [teachersList, setTeachersList] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setTeachersList([...teachersList, formData]);
    setFormData({
      nombres: "",
      apellidos: "",
      correoInstitucional: "",
      numeroCelular: "",
      materia: "",
    });
  };

  return (
    <div>
      <h1>Registro de Profesores</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="nombres"
          placeholder="Nombres"
          value={formData.nombres}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="apellidos"
          placeholder="Apellidos"
          value={formData.apellidos}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="correoInstitucional"
          placeholder="Correo Institucional"
          value={formData.correoInstitucional}
          onChange={handleChange}
          required
        />
        <input
          type="tel"
          name="numeroCelular"
          placeholder="Número de Celular"
          value={formData.numeroCelular}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="materia"
          placeholder="Materia"
          value={formData.materia}
          onChange={handleChange}
          required
        />
        <button type="submit">Registrar</button>
      </form>
      <ul>
        {teachersList.map((teacher, index) => (
          <li key={index}>
            {teacher.nombres} {teacher.apellidos} - {teacher.materia}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeacherRegistration;
