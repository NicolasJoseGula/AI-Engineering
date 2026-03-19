def is_non_negative(value):
    # Returns True if the value is zero or positive
    return value >= 0

def calculate_discount(original_price, discount_rate):
    # Calculates the discount amount based on the original price
    discount_amount = original_price * discount_rate / 100

    # Calculates the price after applying the discount
    discounted_price = original_price - discount_amount

    # Returns both the discounted price and the discount amount
    return discounted_price, discount_amount

def calculate_vat(discounted_price, vat_rate):
    # Calculates the VAT amount based on the discounted price
    vat_amount = discounted_price * vat_rate / 100

    # Calculates the subtotal after adding VAT
    subtotal_with_vat = discounted_price + vat_amount

    # Returns both the subtotal with VAT and the VAT amount
    return subtotal_with_vat, vat_amount

def calculate_tip(subtotal_with_vat, tip_rate):
    # Calculates the tip amount based on the subtotal with VAT
    tip_amount = subtotal_with_vat * tip_rate / 100

    # Calculates the final total after adding the tip
    final_total = subtotal_with_vat + tip_amount

    # Returns both the final total and the tip amount
    return final_total, tip_amount

def get_non_negative_number(message):
    # Requests a numeric value from the user
    value = float(input(message))

    # Validates that the value is not negative
    if not is_non_negative(value):
        raise ValueError("Value cannot be less than zero.")

    # Returns the validated value
    return value

def display_summary(
    original_price,
    discount_rate,
    vat_rate,
    tip_rate,
    discount_amount,
    discounted_price,
    vat_amount,
    subtotal_with_vat,
    tip_amount,
    final_total,
):
    # Displays the final bill summary in a clean format
    print("\n--- Smart Bill Summary ---")
    print(f"Base price:           ${original_price:.2f}")
    print(f"Discount rate:        {discount_rate:.2f}%")
    print(f"Discount amount:      ${discount_amount:.2f}")
    print(f"Price after discount: ${discounted_price:.2f}")
    print(f"VAT rate:             {vat_rate:.2f}%")
    print(f"VAT amount:           ${vat_amount:.2f}")
    print(f"Price with VAT:       ${subtotal_with_vat:.2f}")
    print(f"Tip rate:             {tip_rate:.2f}%")
    print(f"Tip amount:           ${tip_amount:.2f}")
    print(f"Final total:          ${final_total:.2f}")

def main():
    try:
        # Gets the original product price from the user
        original_price = get_non_negative_number(
            "Insert the base price of the product: "
        )

        # Gets the discount percentage from the user
        discount_rate = get_non_negative_number(
            "Insert the discount percentage of the product: "
        )

        # Gets the VAT percentage from the user
        vat_rate = get_non_negative_number(
            "Insert the VAT percentage of the product: "
        )

        # Gets the tip percentage from the user
        tip_rate = get_non_negative_number(
            "Insert the tip percentage of the product: "
        )

    except ValueError as error:
        # Displays the validation error and stops the program
        print(error)
        return

    # Calculates the discounted price and discount amount
    discounted_price, discount_amount = calculate_discount(
        original_price, discount_rate
    )

    # Calculates the subtotal with VAT and VAT amount
    subtotal_with_vat, vat_amount = calculate_vat(discounted_price, vat_rate)

    # Calculates the final total and tip amount
    final_total, tip_amount = calculate_tip(subtotal_with_vat, tip_rate)

    # Displays all calculation results
    display_summary(
        original_price,
        discount_rate,
        vat_rate,
        tip_rate,
        discount_amount,
        discounted_price,
        vat_amount,
        subtotal_with_vat,
        tip_amount,
        final_total,
    )


if __name__ == "__main__":
    # Runs the program
    main()