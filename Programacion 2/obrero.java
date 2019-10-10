public class Obrero{
    private String Nombre;
    private String Rut;
    private int Tarifa;
    private int Descuento;
    private int Horas;

    public void Obrero(String n, String r, int t, int d, int h){
        setNombre(n);
        setRut(r);
        setTarifa(t);
        setDescuento(d);
        setHoras(h);
    }
    public String getNombre(){
        return this.Nombre;
    }
    public void setNombre(String n){
        this.Nombre = n;
    }
    public String getRut(){
        return this.Rut;
    }
    public void setRut(String r){
        this.Rut = r;
    }
    public int getTarifa(){
        return this.Tarifa;
    }
    public void setTarifa(int t){
        this.Tarifa = t;
    }
    public int getDescuento(){
        return this.Descuento;
    }
    public void setDescuento(int d){
        this.Descuento = d;
    }
    public int getHoras(){
        return this.Horas;
    }
    public void setHoras(int h){
        this.Horas = h;
    }
    public int pago(){
        int total = getHoras()*getTarifa();
        if(getHoras() > 40){
            total = total + (int)(getHoras() - 40)*getTarifa/2;
        }
        total = total - (int)total*getDescuento()/100;
        return total;
    }
}

public class AppObrero{
    public static void main(String[] args){
        Obrero o1 = new Obrero("yayo", "12345567-k", 2000, 5, 45);
        System.out.println(o1.getNombre());
        System.out.println(o1.pago());
        x.setHoras(42);
        System.out.println(o1.getHoras);
    }
}
