import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);

    System.out.println("What amount of FizzBuzz you want to generate: ");
    int num = scanner.nextInt();

    System.out.println("\n");

    for (int i = 1; i < num+1; i++) {
      System.out.println(fizzbuzz_check(i));
    }
  }

  public static Boolean is_multiplier(int num, int multiplier) {
    return num % multiplier == 0;
  }

  public static String fizzbuzz_check(int number) {
    String out = "";

    if (is_multiplier(number, 3)) {
      out += "Fizz";
    }
    if (is_multiplier(number, 5)) {
      out += "Buzz";
    }

    if (out.equals("")) {
      return String.valueOf(number);
    }
    return out;
  }

}
