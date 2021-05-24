
CREATE TABLE Medicos
(
    Dni VARCHAR(9),
    Nombre VARCHAR(20),
    Apellidos VARCHAR(50),
    Direccion VARCHAR(20),
    Telefono VARCHAR(9),
    FechaColegiacion DATE,
    CONSTRAINT pk_medicos PRIMARY KEY(Dni)
);
  
CREATE TABLE Pacientes
(
    Dni VARCHAR(9),
    Nombre VARCHAR(20),
    Apellidos VARCHAR(50),
    Direccion VARCHAR(20),
    Telefono VARCHAR(9),
    NumHistorial VARCHAR(4),
    DniMedico VARCHAR(9),
    CONSTRAINT pk_pacientes PRIMARY KEY(Dni),
    CONSTRAINT fk_medicos FOREIGN KEY(DniMedico) REFERENCES Medicos
);

  
CREATE TABLE HorasdeConsulta
(
    DniMedico VARCHAR(9),
    CodigoSala VARCHAR(8),
    Dia VARCHAR(10),
    HoraInicio TIME,
    HoraFin TIME,
    CONSTRAINT fk_medicos2 FOREIGN KEY(DniMedico) REFERENCES Medicos,
    CONSTRAINT pk_horas PRIMARY KEY(DniMedico,CodigoSala)
);

  
CREATE TABLE SalasdeConsultas
(
    Codigo VARCHAR(8),
    Nombre VARCHAR(20),
    Ubicacion VARCHAR(10),
    CONSTRAINT pk_salas PRIMARY KEY(Codigo)
);


INSERT INTO Medicos (Dni,Nombre,Apellidos,Direccion,Telefono,FechaColegiacion) VALUES ('12345678A','Francisco','López Garcia','Ave del paraiso','667223554','1992/05/22');

INSERT INTO Pacientes (Dni,Nombre,Apellidos,Direccion,Telefono,NumHistorial,DniMedico) VALUES ('98765432N','Manolo','Gutierrez Recio','Desengaño','611322455','1234','12345678A');

INSERT INTO HorasdeConsulta (DniMedico,CodigoSala,Dia,HoraInicio,HoraFin) VALUES ('12345678A','26810127','Martes','09:00:00','09:20:00');

INSERT INTO SalasdeConsultas (Codigo,Nombre,Ubicacion) VALUES ('20406080','Sala1','Sevilla');

