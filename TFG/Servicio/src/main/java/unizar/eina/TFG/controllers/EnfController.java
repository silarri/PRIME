package unizar.eina.TFG.controllers;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import unizar.eina.TFG.models.EnfModel;
import unizar.eina.TFG.services.EnfService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/enfermedad")
@CrossOrigin(origins = "http://localhost:3000") // Permitir solicitudes desde localhost:3000
public class EnfController {
    @Autowired
    EnfService enfService;

    @GetMapping()
    public ArrayList<EnfModel> obtenerEnfermedad(){
        System.out.println("obtenerEnfermedad");
        return enfService.obtenerEnfermedad();
    }

    @PostMapping()
    public EnfModel guardarEnfermedad(@RequestBody EnfModel usuario){
        return this.enfService.guardarEnfermedad(usuario);
    }

    @GetMapping( path = "/{id}")
    public Optional<EnfModel> obtenerUsuarioPorId(@PathVariable("id") Long id) {
        return this.enfService.obtenerPorId(id);
    }

    @DeleteMapping( path = "/{id}")
    public String eliminarPorId(@PathVariable("id") Long id){
        boolean ok = this.enfService.eliminarEnfermedad(id);
        if (ok){
            return "Se eliminó el usuario con id " + id;
        }else{
            return "No pudo eliminar el usuario con id" + id;
        }
    }
    
    @GetMapping("/nombres")
    public List<String> obtenerNombresEnfermedades() {
        return this.enfService.obtenerNombresEnfermedades();
    }

}