package unizar.eina.TFG.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import unizar.eina.TFG.models.MedModel;
import unizar.eina.TFG.services.MedService;

import java.util.List;

@RestController
@RequestMapping("/medicamentos")
@CrossOrigin(origins = "http://localhost:3000") // Permitir solicitudes desde localhost:3000
public class MedController {
    @Autowired
    private MedService medicamentoService;

    @GetMapping()
    public List<MedModel> buscarMedicamentoPorNombre(@RequestParam String nombremedicamento) {
        return medicamentoService.buscarPorNombre(nombremedicamento);
    }
}
