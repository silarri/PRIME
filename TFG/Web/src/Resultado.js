import React, { useState, useRef, useEffect  } from 'react';
import './App.css'; // Importa el archivo CSS
import './auxx.css'; // Importa el archivo CSS
import { useNavigate, useLocation } from 'react-router-dom';
import { Bar, getElementAtEvent } from "react-chartjs-2";
import casaAtras from "./Imagenes/CasaNegra.png";
import cruzAtras from "./Imagenes/CruzBlanca.png";
import Loader from 'react-loaders'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarController,
  BarElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  BarController
);

function Resultado() {

  const [loading, setLoading] = useState(true);

  const location = useLocation();
  const { enfermedad, edad, peso, sexo } = location.state;

  const chartRef = useRef();

  const [labelsMed, setLabelsMed] = useState([])
  const [dataMed, setDataMed] = useState([])

  const data = {
    labels: labelsMed,
    datasets: [
      {
        backgroundColor: [
          '#45a7fd94',
          '#55a7fd94',
          '#65a7fd94',
          '#75a7fd94',
          '#85a7fd94',     
        ],
        borderColor: [
          '#65a7fd',
          '#55a7fd',
          '#65a7fd',
          '#75a7fd',
          '#85a7fd'
        ],
        borderWidth: 1,
        data: dataMed,
      },
    ],
  };

  const options = {
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Confianza',
          font: {
            size: 15, // Tamaño de la letra del título
          },
        },
      },
      x: {
        title: {
          display: true,
          text: 'Medicamentos',
          font: {
            size: 15, // Tamaño de la letra del título
          },
        },
      },
    },
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: 'Título de la Gráfica', // Cambia esto por el título que desees
        font: {
          size: 25, // Tamaño de la letra del título
        },
        padding: {
          top: 0,
          bottom: 25,
        },
      },
    },
  };

  const urlPrediccion = 'http://localhost:8080/ejecutarScript?sexo='+sexo+'&edad='+edad+'&peso='+peso+'&enfermedad='+enfermedad 
  useEffect(() => {
    fetch(urlPrediccion, {
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
      
      // Filtrar los medicamentos con la prediccion "Sensible"
      const medicamentosSensibles = data.filter(med => med.prediccion === "Sensible");

      // Ordenar los medicamentos por precisión (de mayor a menor) y luego por número de filas (de mayor a menor)
      medicamentosSensibles.sort((a, b) => {
          // Si la precisión es igual, ordenar por número de filas
          if (a.precision === b.precision) {
              return b.filas - a.filas;
          }
          // Ordenar por precisión de mayor a menor
          return b.precision - a.precision;
      });

      // Tomar los primeros 5 medicamentos después del ordenamiento
      const top5Medicamentos = medicamentosSensibles.slice(0, 5);

      // Ahora 'top5Medicamentos' contiene los 5 medicamentos con la prediccion "Sensible" y la mayor precisión, considerando también el número de filas
      console.log(top5Medicamentos);
      let labell = [];
      let dataa = [];

      top5Medicamentos.forEach(med => {
        labell.push(med.medicamento)
        dataa.push(med.precision);
      });
      setLabelsMed(labell)
      setDataMed(dataa)
      setLoading(false)
    })
    .catch((error) => {
      console.error('Error al enviar la solicitud:', error);
    });
  }, []);

  const navigate = useNavigate();
  const [selectedMedicine, setSelectedMedicine] = useState(null);

  const [medicamento, setMedicamento] = useState();

  const handleMedicineClick = (label) => {
    const urlDescMedicamento = 'http://localhost:8080/medicamentos?nombremedicamento='+label 
    fetch(urlDescMedicamento, {
      method: 'GET'
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Respuesta del servidor no válida');
      }
      return response.json();
    })
    .then((data) => {
      console.log('Respuesta de la API:', data);
      setMedicamento(data[0])
      setSelectedMedicine(label);
    })
    .catch((error) => {
      console.error('Error al enviar la solicitud:', error);
    });
    
  };

  const goBack = () => {
    navigate(process.env.PUBLIC_URL + '/');
  };
  const cerrar = () => {
    setSelectedMedicine(null)
  };

  if (loading) {
    return  (     
    // <Loader type="pacman" />
    <div class="loader">
    <div class="circles">
      <span class="one"></span>
      <span class="two"></span>
      <span class="three"></span>
    </div>
    <div class="pacman">
      <span class="top"></span>
      <span class="bottom"></span>
      <span class="left"></span>
      <div class="eye"></div>
    </div>
  </div>)
  }
  return (
    <>
      <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css' />
      <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.bundle.min.js'></script>

      <section className="credit-card d-flex flex-column align-items-center" style={{opacity: selectedMedicine ? 0.4 : 1 }}>
        <div className="d-flex justify-content-end align-items-center w-100">
          <img src={casaAtras} alt="Volver" onClick={goBack} style={{ cursor: 'pointer', marginRight:'50px' }} />
        </div>
        <div className="container d-flex flex-column align-items-center justify-content-center">
          <div className="card-box2 bg-white"style={{ display: 'inline-block', top:'80px', position:'absolute' }}>
              <h2 className="text-center" style={{fontFamily: 'Abhaya Libre', fontWeight:'bold', letterSpacing: '1px'}}>PREDICTOR DE MEDICAMENTO EFECTIVO</h2>
          </div>
          <div className="row">
            <div className="col-md-4">
              <div className="card-holder">
                <div className="card-box bg-news2">
                  {/* <div className="row"> */}
                    <div className="col-lg-12">
                      <div className="img-box">
                        <img src="https://bootdey.com/img/Content/avatar/avatar7.png" className="img-fluid" alt="Avatar" style={{width:'200px'}} />
                      </div>
                    </div>
                    <div className="col-lg-12">
                      <div className="card-details mt-5">
                        <h3 className="title">DATOS DEL PACIENTE</h3>
                        <div className="row">
                          <div className="form-group col-sm-7  mt-2">
                            <div className="inner-addon right-addon">
                              <label htmlFor="card-holder">Enfermedad</label>
                              <i className="far fa-user"></i>
                              <input id="enfermedad" type="text" className="form-control" placeholder={enfermedad} aria-label="Card Holder" aria-describedby="basic-addon1"readOnly  />
                            </div>
                          </div>
                          <div className="form-group col-sm-5   mt-2">
                            <label htmlFor="age-input">Edad</label>
                            <div className="input-group expiration-date">
                              <input id="enfermedad" type="text" className="form-control" placeholder={edad+" Años"} aria-label="Card Holder" aria-describedby="basic-addon1"readOnly  />
                            </div>
                          </div>
                          <div className="form-group col-sm-7 mt-2">
                            <div className="inner-addon right-addon">
                              <label htmlFor="weight-input">Peso</label>
                              <i className="far fa-credit-card"></i>
                              <div className="input-group">
                              <input id="enfermedad" type="text" className="form-control" placeholder={peso+" Kg"} aria-label="Card Holder" aria-describedby="basic-addon1"readOnly  />
                              </div>
                            </div>
                          </div>
                          <div className="form-group col-sm-5 mt-2">
                            <label htmlFor="gender">Sexo</label>
                            <input id="enfermedad" type="text" className="form-control" placeholder={sexo} aria-label="Card Holder" aria-describedby="basic-addon1"readOnly  />
                          </div>
                        </div>
                      </div>
                    </div> {/* <!--/col-lg-6 --> */}
                  {/* </div> <!--/row --> */}
                </div>
              </div>
            </div>
            <div className="col-md-8">
              <div className="card-holder">
                <div className="card-box" style={{ backgroundColor: 'white' }}>
                  <div className="row justify-content-center align-items-center">
                    <div className="col-lg-11 mt-5" style={{ width: '170vh', height: '55vh' }}>
                      <Bar
                        ref={chartRef}
                        data={data}
                        options={options}
                        onClick={(event) => {
                          const elems = getElementAtEvent(chartRef.current, event);
                          if (elems.length > 0) {
                            const index = elems[0].index;
                            const label = data.labels[index];
                            handleMedicineClick(label);
                          }
                        }}
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
          </div>

        </div>
      </section>

      <div className="d-flex flex-column justify-content-center align-items-center" style={{ position: 'absolute', top: '200px', left: '550px', zIndex: 5 }}>
        {selectedMedicine && (
        <div className="card-box p-3 d-flex flex-column align-items-center" style={{ width: '800px', height: '600px', backgroundColor: '#313131', position: 'relative' }}>
          <img src={cruzAtras} alt="Cerrar" onClick={cerrar} style={{ cursor: 'pointer', position: 'absolute', top: '10px', right: '10px' }} />
          <h4 className="text-white">Detalles de "{selectedMedicine}"</h4>
          
          <div className="text-white d-flex justify-content-between" style={{ fontWeight: 'normal', marginTop: '70px' }}>
            <div style={{ width: '300px', marginRight: '20px', marginLeft: '50px' }}>
              <p><strong>Nombre:</strong> {medicamento.nombreMedicamento}</p>
              <p><strong>Estado actual:</strong> {medicamento.estadoActual}</p>
              <p><strong>Clase de medicamento:</strong> {medicamento.claseMedicamento}</p>
              <p><strong>Año de primera mención:</strong> {medicamento.añoPrimeraMencion}</p>
              <p><strong>Instituto:</strong> {medicamento.instituto}</p>
              <p><strong>Patente:</strong> {medicamento.patente}</p>
            </div>
            <hr style={{ width: '1px', height: 'auto', border: '1px solid white', margin: '0 20px' }} />
            <div style={{ width: '300px', marginLeft: '20px' }}>
              <p><strong>Nombre en inglés:</strong> {medicamento.nombreMedicamentoIngles}</p>
              <p><strong>Fase de desarrollo más alta:</strong> {medicamento.faseDesarrolloMasAlta}</p>
              <p><strong>Suspensión:</strong> {medicamento.suspension}</p>
              <p><strong>Mecanismo Acc. Patógeno Obj:</strong> {medicamento.mecanismoAccPatogenoObj}</p>
              <p><strong>Información:</strong> {medicamento.info}</p>
            </div>
          </div>



        </div>
        )}
      </div>


    </>
  );
}

export default Resultado;
