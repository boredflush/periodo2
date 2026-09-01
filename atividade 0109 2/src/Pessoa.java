public class Pessoa {

    private String nome;
    private int idade;

    public int getIdade() {
        return idade;
    }

    public String getNome() {
        return nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
//    public void verificarIdade(int valorIdade){
//        if(valorIdade>= 18){
//            System.out.println("voce é maior de idade");
//        }else{
//            System.out.println("voce é menor de idade");
//        }
//    }
    public void verificarIdade(){
        if(idade >=18){
            System.out.println(this.getNome()+ "que possui" + idade + " voce é maior de idade");
        }else{
            System.out.println(this.getNome()+ que possui + idade + " voce é menor de idade");
        }

    }
}
