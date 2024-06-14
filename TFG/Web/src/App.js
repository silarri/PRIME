import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Formulario from './Formulario';
import Resultado from './Resultado';


import './App.css';

const App = () => {
  return (
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={Formulario} />
          <Route path='/resultado' Component={Resultado} />
        </Routes>
      </BrowserRouter>
  );
};

export default App;
