package unizar.eina.TFG.services;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import unizar.eina.TFG.models.EnfModel;
import unizar.eina.TFG.repositories.EnfRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class EnfService {
    @Autowired
    EnfRepository enfRepository;
    
    public ArrayList<EnfModel> obtenerEnfermedad(){
        return (ArrayList<EnfModel>) enfRepository.findAll();
    }

    public EnfModel guardarEnfermedad(EnfModel enfermedad){
        return enfRepository.save(enfermedad);
    }

    public Optional<EnfModel> obtenerPorId(Long id){
        return enfRepository.findById(id);
    }

    public boolean eliminarEnfermedad(Long id) {
        try{
            enfRepository.deleteById(id);
            return true;
        }catch(Exception err){
            return false;
        }
    }

    public List<String> obtenerNombresEnfermedades() {
        return ((Collection<EnfModel>) enfRepository.findAll())
                                   .stream()
                                   .map(EnfModel::getNombreEnfermedad)
                                   .collect(Collectors.toList());
    }
    
}