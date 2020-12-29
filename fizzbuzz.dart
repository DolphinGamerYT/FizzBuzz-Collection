import 'dart:io';

bool is_multiplier(int num, int multiplier) {
  return num % multiplier == 0;
}

int process_fizzbuzz(int num) {
  var stopwatch = new Stopwatch()..start();
  for (int i = 1; i < num+1; i++) {
    var out = "";

    if (is_multiplier(i, 3)) {
      out += "Fizz";
    }
    if (is_multiplier(i, 5)) {
      out += "Buzz";
    }

    if (out == "") {
      print(i);
    } else {
      print(out);
    }
  }
  stopwatch.stop();
  return stopwatch.elapsedMilliseconds;
}

void main() {
    print("What amount of FizzBuzz you want to generate: ");
    var num = int.parse(stdin.readLineSync());
    print("\n");

    int milliseconds = process_fizzbuzz(num);
    print("This took me ${milliseconds}ms.");
}