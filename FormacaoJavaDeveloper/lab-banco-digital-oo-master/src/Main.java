
public class Main {

	public static void main(String[] args) {
		Cliente venilton = new Cliente();
		venilton.setNome("Venilton");
		
		Cliente walter = new Cliente();
		walter.setNome("Walter");
		
		Cliente rene = new Cliente();
		rene.setNome("Rene");
		
		
		Conta cc = new ContaCorrente(venilton);
		Conta poupanca = new ContaPoupanca(venilton);
		
		Conta cc1 = new ContaCorrente(walter);
		Conta poupanca1 = new ContaPoupanca(walter);
		
		Conta cc2 = new ContaCorrente(rene);
		Conta poupanca2 = new ContaPoupanca(rene);


		cc.depositar(100);
		cc.transferir(100, poupanca);
		
		cc.imprimirExtrato();
		poupanca.imprimirExtrato();
		
		cc1.depositar(1300);
		cc1.transferir(350, poupanca1);
		
		cc1.imprimirExtrato();
		poupanca1.imprimirExtrato();
		
		cc2.depositar(3050);
		cc2.transferir(2030, poupanca2);
		
		cc2.imprimirExtrato();
		poupanca2.imprimirExtrato();
	}

}
