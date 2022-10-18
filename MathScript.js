//Opening
console.log("Welcome! What is your name? ");
let userName = prompt();
console.log("Hello there, " + userName + "!");
console.log("Please enjoy using this calculator!");

console.log("I can do two sets of computations!");
console.log(
	"Option a: If you give me two numbers, I can add, subtract, multiple and divide them for you."
);
console.log(
	"Option b: If you give me a list of numbers I can help you find mean, median, and mode"
);

console.log("Please select which option you want to try by entering a or b: ");
let calChoice = prompt();

if (calChoice == "a") {
	var x = prompt("Enter a Value", "0");
	var y = prompt("Enter a Value", "0");
	var num1 = parseFloat(x);
	var num2 = parseFloat(y);

	//addition
	console.log("   ~~Addition~~");

	let additionMessageOne = "If you add ";
	let additionMessageTwo = x;
	let additionMessageThree = "by ";
	let additionMessageFour = y;
	let additionMessageFive = "the answer is: ";
	let additionAnswer = x + y;

	console.log(
		additionMessageOne,
		additionMessageTwo,
		additionMessageThree,
		additionMessageFour,
		additionMessageFive,
		additionAnswer
	);

	//subtraction
	console.log("   ~~Subtraction~~");

	let subtractionMessageOne = "If you subtract ";
	let subtractionMessageTwo = x;
	let subtractionMessageThree = "by ";
	let subtractionMessageFour = y;
	let subtractionMessageFive = "the answer is: ";
	let subtractionAnswer = x - y;

	console.log(
		subtractionMessageOne,
		subtractionMessageTwo,
		subtractionMessageThree,
		subtractionMessageFour,
		subtractionMessageFive,
		subtractionAnswer
	);

	let revsubtractionMessageOne = "If you subtract ";
	let revsubtractionMessageTwo = y;
	let revsubtractionMessageThree = "by ";
	let revsubtractionMessageFour = x;
	let revsubtractionMessageFive = "the answer is: ";
	let revsubtractionAnswer = y - x;

	console.log(
		revsubtractionMessageOne,
		revsubtractionMessageTwo,
		revsubtractionMessageThree,
		revsubtractionMessageFour,
		revsubtractionMessageFive,
		revsubtractionAnswer
	);

	//multiply
	console.log("   ~~Multiplication~~");

	let multiplicationMessageOne = "If you multiply ";
	let multiplicationMessageTwo = x;
	let multiplicationMessageThree = "by ";
	let multiplicationMessageFour = y;
	let multiplicationMessageFive = "the answer is: ";
	let multiplicationAnswer = x * y;

	console.log(
		multiplicationMessageOne,
		multiplicationMessageTwo,
		multiplicationMessageThree,
		multiplicationMessageFour,
		multiplicationMessageFive,
		multiplicationAnswer
	);

	//division
	console.log("   ~~Division~~");

	let divisionMessageOne = "If you divide ";
	let divisionMessageTwo = x;
	let divisionMessageThree = "by ";
	let divisionMessageFour = y;
	let divisionMessageFive = "the answer is: ";
	let divisionAnswer = x / y;

	console.log(
		divisionMessageOne,
		divisionMessageTwo,
		divisionMessageThree,
		divisionMessageFour,
		divisionMessageFive,
		divisionAnswer
	);

	//reverse division
	let revdivisionMessageOne = "If you divide ";
	let revdivisionMessageTwo = y;
	let revdivisionMessageThree = "by ";
	let revdivisionMessageFour = x;
	let revdivisionMessageFive = "the answer is: ";
	let revdivisionAnswer = y / x;

	console.log(
		revdivisionMessageOne,
		revdivisionMessageTwo,
		revdivisionMessageThree,
		revdivisionMessageFour,
		revdivisionMessageFive,
		revdivisionAnswer
	);

	console.log("Have a great day!");
} else {
	var groupLength = prompt("How many numbers do you need to work with?");
	console.log("This function still in production mode. Try again later.");
	//console.log("Enter numbers in any order with just a space between: ");

	//let numList = list(map(float, input().split()));
	//numList.sort();

	//console.log("   ~~Ordered List~~");
	//console.log(*numList);

	//console.log("   ~~Mean~~");
	//console.log(statistics.mean(numList));

	//console.log("   ~~Median~~");
	//console.log(statistics.median(numList));

	//console.log("   ~~Mode~~");
	//let mode = statistics.mode(numList);
	//  if (mode == min(numList)) {
	//  console.log("All numbers are unique. No mode.");
	//  } else {
	//  console.log(mode);}

	//console.log("   ~~Range~~");
	//console.log(max(numList) - min(numList));
}
