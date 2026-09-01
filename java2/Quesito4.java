import java.time.Year;
public class Quesito4 {
public static void main(String[] args) {

Carro meuCarro = new Carro();
meuCarro.modelo = "Civic";
meuCarro.ano = 2018;
meuCarro.cor = "Preto";

meuCarro.exibeFichaTecnica();


System.out.println("Idade do carro: " + meuCarro.calculaIdade() + " anos");
}
}


class Carro {
String modelo;
int ano;
String cor;

public void exibeFichaTecnica() {
System.out.println("Modelo: " + modelo);
System.out.println("Ano: " + ano);
System.out.println("Cor: " + cor);
}

public int calculaIdade() {

int anoAtual = Year.now().getValue();

return anoAtual - ano;

}
}