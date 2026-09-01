public class Quesito2 {
public static void main(String[] args) {

Calculadora calc = new Calculadora();

double resultado = calc.dobrarNumero(5);

System.out.println("O dobro e: " + resultado);
}
}
class Calculadora {
public double dobrarNumero(double numero) {
return numero * 2;


}
}