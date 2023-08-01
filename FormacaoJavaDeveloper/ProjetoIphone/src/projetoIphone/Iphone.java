package projetoIphone;

public class Iphone implements ReprodutorMusical, AparelhoTelefonico, NavegadorInternet {
	
	 public void tocar() {
	        System.out.println("Música tocando...");
	    }

	    public void pausar() {
	        System.out.println("Música pausada.");
	    }

	    public void selecionarMusica(String musica) {
	        System.out.println("Música selecionada.");
	    }
	    
	    public void reproduzirMusica(String musica) {
	        System.out.println("Reproduzindo a música: " + musica);
	    }


	    public void ligar(String ligando) {
	        System.out.println("Ligando...");
	    }

	    public void atender() {
	        System.out.println("Atendendo chamada...");
	    }

	    public void iniciarCorreioVoz() {
	        System.out.println("Iniciando correio de voz...");
	    }

	    public void exibirPagina(String url) {
	        System.out.println("Exibindo página...");
	    }

	    public void adicionarNovaAba(String url) {
	        System.out.println("Nova aba adicionada.");
	    }

	    public void atualizarPagina() {
	        System.out.println("Página atualizada.");
	    }

	}

		
	    

	


