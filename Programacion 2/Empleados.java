
public class Empleado{
    private String rut;
    private String nombre;
    private int edad;
    private char genero;
    private int sueldo;
     //Metodos constructores
    public Empleado(){
     this.rut = "";
     this.nombre = "";
     this.edad = 0;
     this.genero = ' ';
     this.sueldo= 0;
    }
    public Empleado(String r, String n, int e, char g, int s){
     this.rut = r;
     this.nombre = n;
     this.edad = e;
     this.genero = g;
     this.sueldo= s;
    }

     //Metodos setters
    public void setRut(String newRut){
        this.rut = newRut;
    }
    public void setNombre(String newNom){
        this.nombre = newNom;
    }
    public void setEdad(int newEd){
        this.edad = newEd;
    }
    public void setGenero(char newgen){
        this.genero = newgen;
    }
    public void setSueldo(int newSueldo){
        this.sueldo = newSueldo;
    }

     //Metodos getters
    public String getRut(){
        return this.rut;
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getEdad() {
        return this.edad;
    }
    public char getGenero(){
        return this.genero;
    }
    public int getSueldo(){
        return this.sueldo;
    }

     //Metodo impresión (muestra estado del objeto)
    public void imprimirDatosEmpleado(){
        System.out.println("Valor del Rut   : "+getRut());
        System.out.println("Valor del Nombre: "+getNombre());
        System.out.println("Valor de la Edad: "+getEdad());
        System.out.println("Valor del Género: "+getGenero());
        System.out.println("Valor del Sueldo: "+getSueldo());
    }

     //Metodos Customers
     public void aumentarSueldo(int porc){
         int aumento = (int)sueldo*porc/100;
         setSueldo(getSueldo()+aumento);
     }
     public int DescuentoAFP(int porcentaje){
         int descuento = (int)getSueldo()*porcentaje/100;
         return descuento;
     }
     public int DescuentoISAPRE(int porcentaje){
         int descuento = (int)getSueldo()*porcentaje/100;
         return descuento;
     }
     public void liquidacion(int AFP, int ISAPRE){
         System.out.println("-------- LIQUIDACION DE SUELDO --------");
         System.out.println("Nombre: " + getNombre());
         System.out.println("Rut: " + getRut());
         System.out.println("Sueldo bruto: " + getSueldo());
         System.out.println("Descuento AFP: " + DescuentoAFP(AFP));
         System.out.println("Descuento ISAPRE: " + DescuentoISAPRE(ISAPRE));
         int descuento = DescuentoAFP(AFP) + DescuentoISAPRE(ISAPRE);
         int liquido = getSueldo() - descuento;
         System.out.println("Descuento total: " + descuento);
         System.out.println("Sueldo Liquido: " + liquido);
     }
}
