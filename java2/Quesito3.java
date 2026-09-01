public class Quesito3 {
public static void main(String[] args) {
Musica minhaMusica = new Musica();

minhaMusica.titulo = "Plastic Love";
minhaMusica.artista = "Mariya Takeuchi";
minhaMusica.anoLancamento = 1984;
minhaMusica.exibeFichaTecnica();
minhaMusica.avalia(10);
minhaMusica.avalia(9.5);

System.out.println("Media de avaliacoes: " + minhaMusica.pegaMedia());
}
}
 class Musica {

String titulo;
String artista;
int anoLancamento;
double avaliacao;
int numAvaliacoes;

public void exibeFichaTecnica() {
System.out.println("Titulo: " + titulo);

System.out.println("Artista: " + artista);

System.out.println("Ano de Lancamento: " + anoLancamento);

}


public void avalia(double nota) {
avaliacao += nota;
numAvaliacoes++;

}

public double pegaMedia() {
if (numAvaliacoes == 0) return 0;
    return avaliacao / numAvaliacoes;

}
}
