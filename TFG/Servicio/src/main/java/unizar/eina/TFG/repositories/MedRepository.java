package unizar.eina.TFG.repositories;

import java.util.List;

import unizar.eina.TFG.models.MedModel;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MedRepository extends CrudRepository<MedModel, Long> {
    List<MedModel> findByNombreMedicamentoContainingIgnoreCase(String nombremedicamento);
}