
def validate_negative_values(value):
    if value < 0:
        return False
    else:
        return True
    
def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

def calculate_iva(price, iva):
    
    return True

def calculate_tip():
    return False

def calcuate_full_buy():
    return False

def show_resume():
    print("Hi")

def main():
    base_price = int(input("Insert the base price of the product: "))
    
    if(validate_negative_values(base_price)):
        discount_percentage = int(input("Insert the discount percentage of the product: "))
        
        if(validate_negative_values(discount_percentage)):
            vat_percentage = int(input("Insert the VAT percentage of the product: "))
            
            if(validate_negative_values(vat_percentage)):
                tip_percentage = int(input("Insert the tip percentage of the product: "))
                
                if(validate_negative_values(tip_percentage)):
                    # TODO Logic Business Here 
                    
                    final_price = calculate_discount(base_price, discount_percentage)
                    
                    calculate_iva(final_price, vat_percentage)
                    
                    calculate_tip()
                    
                    calcuate_full_buy()
                    
                    show_resume()
                    
                else:
                    print("The tip cannot be less than zero. Bye Bye")
            else:
                print("The vat cannot be less than zero. Bye Bye")
        else:
            print("The discount cannot be less than zero. Bye Bye")
    else:
        print("The price cannot be less than zero. Bye Bye")


if __name__ == "__main__":
    main()


