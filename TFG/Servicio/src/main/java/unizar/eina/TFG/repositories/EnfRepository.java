package unizar.eina.TFG.repositories;

import unizar.eina.TFG.models.EnfModel;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EnfRepository extends CrudRepository<EnfModel, Long> {
    
}