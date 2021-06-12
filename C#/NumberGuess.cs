using System;
//Funny thing: I don't actually know if this code works					
public class NumberGuess
{
	public static void Main()
	{
		Random r = new Random();
		
		int ranNum = r.Next(0,100);
		bool outcome = false;
		
		while(outcome == false) {
			Console.WriteLine("Enter a number between 0 and 100: ");
			string n = Console.ReadLine();
			int num = int.Parse(n);
			if (num == ranNum) {
				Console.WriteLine("You have guessed the number!");
				outcome = true;
		}
			else if (num > ranNum) {
				Console.WriteLine("Too high, guess a lower number.");
		}
