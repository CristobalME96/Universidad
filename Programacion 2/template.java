//CLASE (reemplazar Tipo_Atributo por el tipo a usar, como String, int, char, float, etc)
public class NombreClase{
// ATRIBUTOS
    private Tipo Nombre_Atributo;
// CONSTRUCTOR CON PARAMETROS
    public void NombreClase(Tipo Nombre_Atributo_n){
        setNombre_Atributo(Nombre_Atributo_n);
    }
// CONSTRUCTOR VACIO O SIN PARAMETROS
    public void NombreClase(){
        setNombre_Atributo("algo");
    }
// METODO GET
    public Tipo getNombre_Atributo(){
        return this.Nombre_Atributo;
    }
// METODO SET
    public void setNombre_Atributo(Tipo Nombre_Atributo_n){
        this.Nombre_Atributo = Nombre_Atributo_n;
    }
// METODO CUSTOM SEGUN SEA REQUERIDO
    public Tipo Metodo_Custom(){
        //lo que se pida para el metodo
    }

    public void ImprimirDatosNombreClase(){
        System.out.println(getNombre_Atributo());
    }
}

// PROGRAMA PRINCIPAL EN QUE SE UTILIZARA LA CLASE
public class AppNombreClase{
    public static void main(String[] args){
// CONTENIDO DEL PROGRAMA PRINCIPAL
        String Rut = "123468-k";
        NombreClase obj1 = new NombreClase(Rut);
        NombreClase obj2 = new NombreClase();
        System.out.println("lo que quieras imprimir");
        System.out.println(obj1.getNombre_Atributo());
        obj1.setNombre_Atributo("nuevo valor");
    }
}
