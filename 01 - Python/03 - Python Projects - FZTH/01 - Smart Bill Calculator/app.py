def is_non_negative(value):
    return value >= 0

def calculate_discount(original_price, discount_rate):
    discount_amount = original_price * discount_rate / 100
    discounted_price = original_price - discount_amount
    return discounted_price, discount_amount

def calculate_vat(discounted_price, vat_rate):
    vat_amount = discounted_price * vat_rate / 100
    subtotal_with_vat = discounted_price + vat_amount
    return subtotal_with_vat, vat_amount

def calculate_tip(subtotal_with_vat, tip_rate):
    tip_amount = subtotal_with_vat * tip_rate / 100
    final_total = subtotal_with_vat + tip_amount
    return final_total, tip_amount

def get_non_negative_number(message):
    value = float(input(message))
    
    if not is_non_negative(value):
        raise ValueError("Value cannot be less than zero.")
    
    return value

def display_summary(
    original_price,
    discount_rate,
    vat_rate,
    tip_rate,
    discounted_price,
    discount_amount,
    subtotal_with_vat,
    vat_amount,
    final_total,
    tip_amount,
):
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
        original_price = get_non_negative_number("Insert the base price of the product: ")

        discount_rate = get_non_negative_number("Insert the discount percentage of the product: ")

        vat_rate = get_non_negative_number("Insert the VAT percentage of the product: ")

        tip_rate = get_non_negative_number("Insert the tip percentage of the product: ")
        
    except ValueError as error:
        print(error)
        return

    discounted_price, discount_amount = calculate_discount(original_price, discount_rate)
    subtotal_with_vat, vat_amount = calculate_vat(discounted_price, vat_rate)
    final_total, tip_amount = calculate_tip(subtotal_with_vat, tip_rate)

    display_summary(
                    original_price,
                    discount_rate,
                    vat_rate,
                    tip_rate,
                    discounted_price,
                    discount_amount,
                    subtotal_with_vat,                        
                    vat_amount,
                    final_total,
                    tip_amount,
                    )

if __name__ == "__main__":
    main()