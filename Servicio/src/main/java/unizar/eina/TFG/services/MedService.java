package unizar.eina.TFG.services;

import unizar.eina.TFG.models.MedModel;
import unizar.eina.TFG.repositories.MedRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class MedService {
    @Autowired
    private MedRepository medicamentoRepository;

    public List<MedModel> buscarPorNombre(String nombremedicamento) {
        return medicamentoRepository.findByNombreMedicamentoContainingIgnoreCase(nombremedicamento);
    }
}
