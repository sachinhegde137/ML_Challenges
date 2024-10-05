from math import gcd

if __name__ == '__main__':
    total_outcomes = 6 * 6


    favorable_outcomes = 0
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 + die2 <= 9:
                favorable_outcomes += 1

    gcd_value = gcd(favorable_outcomes, total_outcomes)
    simplified_numerator = favorable_outcomes // gcd_value
    simplified_denominator = total_outcomes // gcd_value

    print(f"{simplified_numerator}/{simplified_denominator}")
