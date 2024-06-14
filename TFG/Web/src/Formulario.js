import React, { useState, useEffect } from 'react';
import './App.css'; // Importa el archivo CSS
import Select from 'react-select';
import mujer from './Imagenes/mujer.png';
import hombre from './Imagenes/hombre.png';
import { useNavigate } from 'react-router-dom';


function Formulario() {
  const navigate = useNavigate();

  const [enfOptions, setEnfOptions] = useState([
    { value: 'nada', label: 'Selecciona una enfermedad' }
  ]);

  const urlListaEnfermedades = 'http://localhost:8080/enfermedad/nombres'  
  useEffect(() => {
    fetch(urlListaEnfermedades, {
      method: 'GET',
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Respuesta del servidor no válida');
      }
      return response.json();
    })
    .then((data) => {
      console.log('Respuesta de la API:', data);


      let enfermedades = [];

      data.forEach(enf => {
        const nuevoEvento = {
            value: enf,
            label: enf
          };
          enfermedades.push(nuevoEvento);
      });
      //console.log(eventosFormateados);
      setEnfOptions(enfermedades)
    })
    .catch((error) => {
      console.error('Error al enviar la solicitud:', error);
    });
  }, []);
  const customStyles = {
    option: (provided, state) => ({
      ...provided,
      fontWeight: state.isSelected ? 'normal' : 'normal',
    }),
    singleValue: (provided, state) => ({
      ...provided,
      fontWeight: 'normal',
    }),
  };

  // Estado para almacenar los valores de los campos del formulario
  const [formData, setFormData] = useState({
    enfermedad: '',
    edad: '',
    peso: '',
    sexo: 'masculino',
  });

  // Función para manejar el cambio en los campos del formulario
  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.id]: e.target.value,
    });
  };

  // Función para manejar el envío del formulario
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Comprueba si todos los campos están completos antes de redirigir
    if (formData.enfermedad && formData.edad && formData.peso && formData.sexo) {
      // Redirige a otra página
      navigate(process.env.PUBLIC_URL+ '/resultado', {state:{enfermedad: formData.enfermedad, edad: formData.edad, peso: formData.peso, sexo: formData.sexo} });
    } else {
      // Si falta algún campo, muestra un mensaje de error o toma alguna otra acción
      console.log('Por favor, completa todos los campos.',formData.enfermedad, formData.edad, formData.peso, formData.sexo)
      alert('Por favor, completa todos los campos.');
    }
  };

  return (
    <>
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css'/>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.bundle.min.js'></script>

    <section className="credit-card">
        <div className="container d-flex flex-column align-items-center">
            <div className="card-box2 bg-white"style={{ display: 'inline-block' }}>
                <h2 className="text-center" style={{fontFamily: 'Abhaya Libre', fontWeight:'bold', letterSpacing: '1px'}}>PREDICTOR DE MEDICAMENTO EFECTIVO</h2>
            </div>
            <div className="card-holder">
                <div className="card-box bg-news">
                    <div className="row">
                        <div className="col-lg-6">
                            <div className="img-box">
                            {/* <img src={mujer} alt="GIF" className="img-fluid" style={{ width: '50%', marginLeft:'-50px' }}/> */}
                            <img src="https://bootdey.com/img/Content/avatar/avatar7.png" className="img-fluid" alt="Avatar" />

                            </div>
                        </div>

                        <div className="col-lg-6">
                            <div className="card-details">
                                <h3 className="title">DATOS DEL PACIENTE</h3>
                                <div className="row">

                                <div className="form-group col-sm-7">
                                    <div className="inner-addon right-addon">
                                    <label htmlFor="enfermedad">Enfermedad</label>
                                    <i className="far fa-user"></i>
                                    {/* <input id="card-holder" type="text" className="form-control" placeholder="Card Holder" aria-label="Card Holder" aria-describedby="basic-addon1"/> */}
                                    <Select
                                        type="text"
                                        id="enfermedad"
                                        className="basic-single"
                                        aria-describedby="basic-addon1"
                                        aria-label="Card Holder"
                                        classNamePrefix="select"
                                        defaultValue={enfOptions[0]}
                                        isDisabled={false}
                                        isLoading={false}
                                        isClearable={true}
                                        isRtl={false}
                                        isSearchable={true}
                                        name="Enfermedad"
                                        options={enfOptions}
                                        styles={customStyles}
                                        onChange={(selectedOption) => {
                                            if (selectedOption) {
                                                setFormData({ ...formData, enfermedad: selectedOption.value });
                                            } else {
                                                setFormData({ ...formData, enfermedad: '' }); // Si se quita la opción seleccionada, establece el valor en una cadena vacía
                                            }
                                        }}
                                    />
                                    </div>	
                                </div>

                                <div className="form-group col-sm-5">
                                    <label htmlFor="edad">Edad</label>
                                    <div className="input-group expiration-date">
                                    <input
                                        type="number"
                                        className="form-control"
                                        id="edad"
                                        placeholder="Edad"
                                        aria-label="Edad"
                                        aria-describedby="basic-addon1"
                                        min="0"
                                        max="120"
                                        value={formData.edad}
                                        onChange={handleInputChange}
                                    />
                                    <div className="input-group-append">
                                        <span className="input-group-text">Años</span>
                                    </div>
                                    </div>
                                </div>

                                <div className="form-group col-sm-7">
                                    <div className="inner-addon right-addon">
                                    <label htmlFor="weight-input">Peso</label>
                                    <i className="far fa-credit-card"></i>
                                    <div className="input-group">
                                        <input
                                        id="peso"
                                        type="number"
                                        className="form-control"
                                        placeholder="Peso"
                                        aria-label="Peso"
                                        aria-describedby="basic-addon1"
                                        min="0"
                                        step="0.1" // Cambia este valor según tus necesidades de precisión
                                        value={formData.peso}
                                        onChange={handleInputChange}
                                        />
                                        <div className="input-group-append">
                                        <span className="input-group-text">Kg</span>
                                        </div>
                                    </div>
                                    </div>
                                </div>

                                <div className="form-group col-sm-5">
                                    <label htmlFor="gender">Sexo</label>
                                    <select id="sexo" className="form-control" value={formData.sexo} onChange={handleInputChange}>
                                    <option value="Masculino">Masculino</option>
                                    <option value="Femenino">Femenino</option>
                                    </select>
                                </div>

                                <div className="form-group col-sm-12">
                                    <button  className="btn btn-primary btn-block" style={{letterSpacing: '1px'}} onClick={handleSubmit}>PREDECIR</button>
                                </div>
                                
                                </div>
                            </div>				
                        </div>{/* <!--/col-lg-6 -->  */}
                    </div> {/* <!--/row --> */}
                </div>
            </div>{/* <!--/card-holder -->		  */}
        </div>{/* <!--/container --> */}
		</section>
    </>
  );
}

export default Formulario;