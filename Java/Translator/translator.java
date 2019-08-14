import java.util.Scanner;
import java.util.ArrayList;
import java.util.random;

public class translator {
    public static void main(String[] args) {

        String output = "";
        Scanner.in = new Scanner(System.in);
        ArrayList alphabet = new ArrayList<String>("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "X", "Y", "Z",
                                                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "x", "y", "z");

        ArrayList possibillities = new ArrayList<String>("BC", "AC", "AB", "EF", "DF", "DE", "HI", "GI", "GH", "AX", "DT", "GP", "IS", "FV", "CZ", "XT", "PS", "IM", "KD", "RY", "SZ", "AJ", "XZ", "SV",
                                                        "JX", "EH", "OZ", "AG", "BH", "IC", "LP", "BE", "FC", "KL", "JL", "JK", "NO", "MO", "MN", "GL", "UY", "VZ", "UV", "TV", "FN", "YZ", "RU", "CO",
                                                        "DG", "AC", "IF", "KT", "FD", "ED", "IH", "IG", "HG", "XA", "TD", "PG", "SI", "VF", "ZC", "LG", "SP", "MI", "DK", "YR", "ZS", "JA", "UR", "VS",
                                                        "CB", "HE", "ZO", "FE", "FD", "NV", "AD", "GI", "GH", "AX", "DT", "GP", "IS", "FV", "CZ", "RS", "PS", "IM", "XP", "RY", "FN", "TP", "XZ", "XY", 
                                                        "XY", "AC", "BA", "GA", "HB", "CI", "PL", "IG", "HG", "LK", "LJ", "KJ", "ON", "OM", "NM", "TX", "YU", "ZV", "VU", "VT", "NF", "ZY", "ZX", "OC",
                                                        "GD", "HE", "ZO", "TK", "DF", "VN", "DA", "EB", "MS", "AX", "DT", "GP", "NO", "FV", "CZ", "SR", "PS", "RP", "PX", "RY", "UT", "PT", "RU", "YX");

        System.out.println("Do you want to translate or encrypt?(Translate/Encrypt)");
        String answer = in.nextLine();

        if (answer.equals("encrypt") || answer.equals("Encrypt") || answer.equals("ENCRYPT")){
            System.out.println("Enter a text for encryption: ");
            String text = in.nextLine();

            for(int i; i < text.length(); i++){

                for(int o; o < alphabet.size(); o++){
                    Random rand = new Random(5);

                    if(text.charAt(i) == alphabet.get(o) || text.charAt(i) == alphabet.get(o + 24)){
                        String semi = possibillities.get(o + (24 * rand)) + "-";
                        output = output + semi;
                    }
                }
            }
        }

        else if(answer.equals("translate") || answer.equals("Translate") || answer.equals("TRANSLATE")){
            System.out.println("Enter a text to transalte: ");
            String text = in.nextLine();


            for(int i; i < text.length(); i = i + 2){
                String semi_text = text.substring(i, i + 1);

                for(int o; o < 24; o++){
                    
                    if(semi_text.equals(possibilities.get(o)) || semi_text.equals(possibilities.get(o + 24)) || semi_text.equals(possibilities.get(o + 48)) || semi_text.equals0(possibilities.get(o + 72)) || semi_text.equals(possibilities.get(o + 96)) ||semi_text.equals(possibilities.get(o + 120))){
                        output = output + alphabet.get(o);
                    }
                }
            }
        }

        else {
            System.out.println("Self-destruction terminated");
        }

        if(!output.equals("")){
            System.out.println(output);
        }
    }
}