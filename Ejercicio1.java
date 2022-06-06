Ejercicio 1

Autor: Jhiovany Moreno Gamez

public class verificarAnagramas
{

     public static void main(String []args)
	 {
		String cadena1 = new String("ballena");
		String cadena2 = new String("llenaba");
	
		char[] ordenarCadena1= cadena1.toCharArray();
		java.util.Arrays.sort(ordenarCadena1);
		String palabra1 = new String(ordenarCadena1);
	
		char[] ordenarCadena2= cadena2.toCharArray();
		java.util.Arrays.sort(ordenarCadena2);
		String palabra2 = new String(ordenarCadena2);
	
		if (palabra1.equals(palabra2))
			System.out.println("Son Anagramas");
		
		else
			System.out.println("No Son Anagramas");		
	}
}