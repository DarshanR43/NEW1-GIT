def process_purchase(purchase_entry):
    """Processes a single purchase entry into structured data."""
    parts = purchase_entry.split(',')
    
    #@start-editable@
    
    customer_id = int(parts[0])
    purchase_type = parts[1] if len (parts[1])>0 else 'unknown_mode'
    purchase_amount = int(parts[2])
    #@end-editable@

    return customer_id, purchase_type, purchase_amount

def create_purchase_summary(purchases):
    """Compiles a summary of total purchases per customer and categorizes customers by purchase types."""
    total_purchases = {}
    customers_per_type = {'store': [], 'online': [], 'unknown_mode': []}
    #@start-editable@
    lst=[]
    for i in purchases:
        customers_per_type[i[1]].append(i[0])
    for i in purchases:
        if i[0] not in lst:
            lst.append(i[0])
    for i in lst:
        price=0
        for j in purchases:
            if i==j[0]:
                price+=j[2]
        total_purchases[i]=price           
    
    # ____________ Enter your code here... _______________
    #@end-editable@

    return total_purchases, customers_per_type

def identify_top_spender(purchase_summary):
    """Identifies the customer ID of the top spender."""
    
    #@start-editable@
    maxi=0
    for i in purchase_summary:
        if purchase_summary[i]>maxi:
            maxi=purchase_summary[i]
    for i in purchase_summary:
        if purchase_summary[i]==maxi:
            top_spender=i
                    
        
    #@end-editable@

    return top_spender

# Main block to process the input
def main():
    n = int(input(""))
    purchases = []
    
    #@start-editable@
    for i in range(n):
        purchase_entry = input("")
        l=process_purchase(purchase_entry)
        l=list(l)
        purchases.append(l)
            
    # ____________ Enter your code here... _______________
    #@end-editable@

    total_purchases , customers_per_type = create_purchase_summary(purchases)
    top_spender = identify_top_spender(total_purchases)
    
    print(f"Total purchases per customer: {total_purchases}")
    print(f"Customers per purchase type: {customers_per_type}")
    print(f"Top spender's customer ID: {top_spender}")

if _name_ == "_main_":
    main()