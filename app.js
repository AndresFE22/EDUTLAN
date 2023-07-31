const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Servir archivos estáticos de la landing
app.use('/staticP', express.static(path.join(__dirname, 'staticP')));

// Servir archivos estáticos de los proyectos
app.use('/diccionarioelectronico', express.static(path.join(__dirname, 'proyectos', 'diccionarioelectronico', 'dist')));
app.use('/diccionariokogui', express.static(path.join(__dirname, 'proyectos', 'diccionariokogui', 'dist')));
app.use('/mapa', express.static(path.join(__dirname, 'proyectos', 'mapa', 'dist')));

// Ruta para servir la landing
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Ruta para capturar todas las demás rutas y servir la landing
app.get('*', (req, res) => {
  if (req.url.startsWith('/diccionarioelectronico') ||
      req.url.startsWith('/diccionariokogui') ||
      req.url.startsWith('/mapa')) {
    let projectPath = req.url.split('/')[1];
    res.sendFile(path.join(__dirname, 'proyectos', projectPath, 'dist', 'index.html'));
  } else {
    res.sendFile(path.join(__dirname, 'index.html'));
  }
});

app.listen(port, () => {
  console.log(`Servidor iniciado en http://localhost:${port}`);
});
