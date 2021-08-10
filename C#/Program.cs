using System;

namespace testcs
{
    class Program
{
    static void Main(string[] args)
    {
    static Double Eval(String expression)
    {
    System.Data.DataTable table = new System.Data.DataTable();
    return Convert.ToDouble(table.Compute(expression, String.Empty));
    }
      Console.WriteLine("Enter a number: ");
      Console.WriteLine("Screw you");
      string num1 = Console.ReadLine();
      Console.WriteLine("Screw you");
      Console.WriteLine("Choose one of the four operators\n(+, -, /, *): ");
      string op = Console.ReadLine();
      Console.WriteLine("Enter a second number: ");
      string num2 = Console.ReadLine();
      string exp = (num1 + op + num2);
      double answer;
      answer = Eval(exp);
      Console.WriteLine(answer);
    }
}
}