package unizar.eina.TFG.models;

import jakarta.persistence.*;

@Entity
@Table(name = "Enfermedad")
public class EnfModel {
    @Id
    @Column(name = "idenfermedad") 
    private Long idEnferemdad;

    @Column(name = "nombreenfermedad") 
    private String nombreEnfermedad;

    @Column(name = "mecanismoresistencia") 
    private String mecanismoResistencia;

    // getters and setters
    public Long getId() {
        return idEnferemdad;
    }

    public void setId(Long idEnferemdad) {
        this.idEnferemdad = idEnferemdad;
    }

    public String getNombreEnfermedad() {
        return nombreEnfermedad;
    }

    public void setNombreEnfermedad(String nombreEnfermedad) {
        this.nombreEnfermedad = nombreEnfermedad;
    }
    
    public String getMecanismoResistencia() {
        return mecanismoResistencia;
    }

    public void setMecanismoResistencia(String mecanismoResistencia) {
        this.mecanismoResistencia = mecanismoResistencia;
    }
}
