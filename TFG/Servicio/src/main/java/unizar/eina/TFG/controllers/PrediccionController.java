package unizar.eina.TFG.controllers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import unizar.eina.TFG.models.PrediccionResultado;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/")
@CrossOrigin(origins = "http://localhost:3000") // Permitir solicitudes desde localhost:3000
public class PrediccionController {

    @GetMapping("/ejecutarScript")
    public ResponseEntity<List<PrediccionResultado>> ejecutarScript(@RequestParam String sexo, 
                                                                    @RequestParam int edad, 
                                                                    @RequestParam double peso, 
                                                                    @RequestParam String enfermedad) {
            // Ejecutar el script de Python con los parámetros recibidos
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("py", "C:/Users/rober/OneDrive - unizar.es/Escritorio/TFG/Analisis/Predictor.py", 
            sexo, Integer.toString(edad), Double.toString(peso), enfermedad);
            
            System.out.println("py C:/Users/rober/OneDrive - unizar.es/Escritorio/TFG/Analisis/Predictor.py " + sexo + " " + edad + " " + peso + " " + enfermedad);


            Process process = processBuilder.start();

            // Capturar la salida del script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            List<PrediccionResultado> resultados = new ArrayList<>();
            String line;
            while ((line = reader.readLine()) != null) {
                // Parsear cada línea de salida y crear un objeto PrediccionResultado
                String[] partes = line.split(", ");
                PrediccionResultado resultado = new PrediccionResultado();
                resultado.setMedicamento(partes[0].split(": ")[1]);
                resultado.setPrediccion(partes[1].split(": ")[1]);
                resultado.setPrecision(Double.parseDouble(partes[2].split(": ")[1]));
                resultado.setFilas(Integer.parseInt(partes[3].split(": ")[1]));
                resultados.add(resultado);
            }

            int exitVal = process.waitFor();
            if (exitVal == 0) {
                return ResponseEntity.ok(resultados);
            } else {
                // Si hay algún error al ejecutar el script, devolver un mensaje de error
                return ResponseEntity.status(500).body(null);
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            return ResponseEntity.status(500).body(null);
        }
    }

}