public class Quesito5 {
public static void main(String[] args) {

Aluno aluno1 = new Aluno();
aluno1.nome = "Otavio";
aluno1.idade = 18;
aluno1.exibeInformacoes();
}
}
 class Aluno {

String nome;
int idade;
public void exibeInformacoes() {

System.out.println("Nome do Aluno: " + nome);
System.out.println("Idade: " + idade + " anos");

}
}