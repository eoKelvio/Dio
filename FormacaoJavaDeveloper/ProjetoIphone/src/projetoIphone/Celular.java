package projetoIphone;

public class Celular {

	public static void main(String[] args) {

		Iphone iPhone = new Iphone();
		
		// ReprodutorMusical
        iPhone.reproduzirMusica("Hey Jude");
        iPhone.pausar();
        iPhone.selecionarMusica("Let it Be");
        
        // AparelhoTelefonico
        iPhone.ligar("123456789");
        iPhone.atender();
        iPhone.iniciarCorreioVoz();
        
        // NavegadorInternet
        iPhone.exibirPagina("www.google.com");
        iPhone.adicionarNovaAba("www.youtube.com");
        iPhone.atualizarPagina();
    }
}


