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
	var stringList = [];
	for (var a = 0; a < groupLength; a++) {
		stringList[a] = prompt("Enter a value: " + (a + 1));
	}

	var numList = stringList.map(Number);

	//working sort
	console.log("   ~~Ordered List~~");
	console.log(numList.sort());

	//working min/max
	console.log("   ~~Minimum & Maximum~~");
	console.log("The smallest number is: " + Math.min.apply(Math, numList));
	console.log("The largest number is: " + Math.max.apply(Math, numList));

	//not working mean

	function meanCalc() {
		//let mean = (numList) => {
		//	let total = 0;
		//	for (let i = 0; i < numList.length; i++) {
		//		total += numList[i];
		//	}
		//	return total / numList.length;

		const initialValue = 0;
		const sumWithInitial = numList.reduce(
			(previousValue, currentValue) => previousValue + currentValue,
			initialValue
		);

		const mean = sumWithInitial / numList.length;

		console.log("   ~~Sum~~");
		console.log("The sum of the entered numbers: " + sumWithInitial);

		console.log("   ~~Mean~~");
		console.log(mean);
	}

	//not working median
	console.log("   ~~Median~~");
	const median = (numList) => {
		const { length } = numList;

		numList.sort((a, b) => a - b);

		if (length % 2 === 0) {
			return (numList[length / 2 - 1] + numList[length / 2]) / 2;
		}

		return numList[(length - 1) / 2];
	};
	console.log(median);

	//not working mode
	console.log("   ~~Mode~~");
	const mode = (numList) => {
		const mode = {};
		let max = 0,
			count = 0;

		for (let i = 0; i < numList.length; i++) {
			const item = numList[i];

			if (mode[item]) {
				mode[item]++;
			} else {
				mode[item] = 1;
			}

			if (count < mode[item]) {
				max = item;
				count = mode[item];
			}
		}

		return max;
	};
	console.log(mode);

	//not working range
	console.log("   ~~Range~~");
	const range = (numList) => {
		numList.sort((a, b) => a - b);

		return [numList[0], numList[numList.length - 1]];
	};
	console.log(range);
}
