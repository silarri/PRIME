package unizar.eina.TFG.models;

import jakarta.persistence.*;

@Entity
@Table(name = "Medicamento")
public class MedModel {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "idmedicamento")
    private Long idMedicamento;

    @Column(name = "nombremedicamento", nullable = false)
    private String nombreMedicamento;

    @Column(name = "nombremedicamentoingles", nullable = false)
    private String nombreMedicamentoIngles;

    @Column(name = "clasemedicamento")
    private String claseMedicamento;

    @Column(name = "añomrimera_mencion")
    private String añoPrimeraMencion;

    @Column(name = "instituto")
    private String instituto;

    @Column(name = "estadomctual")
    private String estadoActual;

    @Column(name = "fasedesarrollomasalta")
    private String faseDesarrolloMasAlta;

    @Column(name = "suspension", length = 200)
    private String suspension;

    @Column(name = "mecanismoaccpatogenoobj", length = 500)
    private String mecanismoAccPatogenoObj;

    @Column(name = "info", length = 500)
    private String info;

    @Column(name = "patente", length = 20)
    private String patente;

    
    
    public void setIdMedicamento(Long idMedicamento) {
        this.idMedicamento = idMedicamento;
    }
    public void setNombreMedicamento(String nombreMedicamento) {
        this.nombreMedicamento = nombreMedicamento;
    }
    public void setNombreMedicamentoIngles(String nombreMedicamentoIngles) {
        this.nombreMedicamentoIngles = nombreMedicamentoIngles;
    }
    public void setClaseMedicamento(String claseMedicamento) {
        this.claseMedicamento = claseMedicamento;
    }
    public void setAñoPrimeraMencion(String añoPrimeraMencion) {
        this.añoPrimeraMencion = añoPrimeraMencion;
    }
    public void setInstituto(String instituto) {
        this.instituto = instituto;
    }
    public void setEstadoActual(String estadoActual) {
        this.estadoActual = estadoActual;
    }
    public void setFaseDesarrolloMasAlta(String faseDesarrolloMasAlta) {
        this.faseDesarrolloMasAlta = faseDesarrolloMasAlta;
    }
    public void setSuspension(String suspension) {
        this.suspension = suspension;
    }
    public void setMecanismoAccPatogenoObj(String mecanismoAccPatogenoObj) {
        this.mecanismoAccPatogenoObj = mecanismoAccPatogenoObj;
    }
    public void setInfo(String info) {
        this.info = info;
    }
    public void setPatente(String patente) {
        this.patente = patente;
    }

    public Long getIdMedicamento() {
        return idMedicamento;
    }
    public String getNombreMedicamento() {
        return nombreMedicamento;
    }
    public String getNombreMedicamentoIngles() {
        return nombreMedicamentoIngles;
    }
    public String getClaseMedicamento() {
        return claseMedicamento;
    }
    public String getAñoPrimeraMencion() {
        return añoPrimeraMencion;
    }
    public String getInstituto() {
        return instituto;
    }
    public String getEstadoActual() {
        return estadoActual;
    }
    public String getFaseDesarrolloMasAlta() {
        return faseDesarrolloMasAlta;
    }
    public String getSuspension() {
        return suspension;
    }
    public String getMecanismoAccPatogenoObj() {
        return mecanismoAccPatogenoObj;
    }
    public String getInfo() {
        return info;
    }
    public String getPatente() {
        return patente;
    }

}
