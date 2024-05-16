# 1. Name:
#      Jay Underwood
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program simulates a decision-making process for purchasing houses and hotels in a Monopoly game.
# 4. What was the hardest part? Be as specific as possible.
#      There wasn't anything too difficult, it was mostly just very tedious due to the number of outcomes possible.
#      The hardest part was probably getting the program to jump to conclusions as soon as possible, such as the moment a user says they don't own all green squares.
# 5. How long did it take for you to complete the assignment?
#      It took me about 3 hours to do this project, spread across a couple of days.

def get_contents(square):
    """
    Get the contents of a given property square in the Monopoly game.
    
    Parameters:
        square (str): The name of the property square.
        
    Returns:
        int: The content of the property square (0-5).
    """
    while True:
        try:
            content = int(input(f"{square} (0 : nothing, 1 : one house, 2 : two houses, 3 : three houses, 4 : four houses, 5 : hotel) "))
            if content < 0 or content > 5:
                print("Invalid input. Please enter a number between 0 and 5.")
            else:
                return content
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_all_info():
    """
    Get all necessary information from the user to make a decision in the Monopoly game.
    
    Returns:
        tuple: A tuple containing the ownership status, property contents, available money, houses, hotels, and cost.
    """
    pc = "What is on Pacific Avenue?"
    nc = "What is on North Carolina Avenue?"
    pa = "What is on Pennsylvania Avenue?"
    
    while True:
        ownership = input("Do you own all the green properties? (y / n) ").lower()
        if ownership == "y":
            ownership = True
            break
        elif ownership == "n":
            ownership = False
            return ownership, None, None, None, None, None, None, None
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    pa_content = get_contents(pa)
    if pa_content == 5:
        return ownership, None, None, pa_content, None, None, None, None
    pc_content = get_contents(pc)
    nc_content = get_contents(nc)
    if pc_content == 5 and pa_content == 4 and nc_content == 4:
        return ownership, pc_content, nc_content, pa_content, None, None, None, None
    if pc_content == 4 and pa_content == 4 and nc_content == 5:
        return ownership, pc_content, nc_content, pa_content, None, None, None, None
    
    cost = 2600 - (200 * pc_content + 200 * nc_content + 200 * pa_content)
    
    while True:
        try:
            money = int(input("How much cash do you have to spend? "))
            if money < 0:
                print("Invalid input. Please enter a positive integer.")
            elif money < cost:
                return ownership, pc_content, nc_content, pa_content, money, None, None, cost
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            houses = int(input("How many houses are there to purchase? "))
            if houses < 0:
                print("Invalid input. Please enter a positive integer.")
            elif houses < (12 - (pc_content + nc_content + pa_content)):
                return ownership, pc_content, nc_content, pa_content, money, houses, None, cost
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            hotels = int(input("How many hotels are there to purchase? "))
            if hotels < 0:
                print("Invalid input. Please enter a positive integer.")
            elif hotels < 1:
                return ownership, pc_content, nc_content, pa_content, money, houses, hotels, cost
            else:
                break
        except ValueError:
            print("Invalid input. Please input an integer.")

    return ownership, pc_content, nc_content, pa_content, money, houses, hotels, cost

def purchase_outputs(pc_content, nc_content, pa_content, cost):
    """
    Generate the output message for purchasing houses and hotels.
    
    Parameters:
        pc_content (int): Content of Pacific Avenue.
        nc_content (int): Content of North Carolina Avenue.
        pa_content (int): Content of Pennsylvania Avenue.
        cost (int): Total cost of the purchase.
        
    Returns:
        str: The purchase message.
    """
    total_houses_needed = 12 - (pc_content + nc_content + pa_content)
    output = f"This will cost ${cost:.2f}.\n    Purchase 1 hotel and {total_houses_needed} house(s).\n    Put 1 hotel on Pennsylvania and return any houses to the bank."

    if nc_content < 4:
        output += f"\n    Put {4 - nc_content} house(s) on North Carolina."

    if pc_content < 4:
        output += f"\n    Put {4 - pc_content} house(s) on Pacific."

    return output

def all_outputs(ownership, pc_content, nc_content, pa_content, money, houses, hotels, cost):
    """
    Determine the final output based on the game state and user inputs.
    
    Parameters:
        ownership (bool): Whether the user owns all green properties.
        pc_content (int): Content of Pacific Avenue.
        nc_content (int): Content of North Carolina Avenue.
        pa_content (int): Content of Pennsylvania Avenue.
        money (int): Available cash.
        houses (int): Number of available houses.
        hotels (int): Number of available hotels.
        cost (int): Total cost of the purchase.
        
    Returns:
        str: The final output message.
    """
    if ownership == False:
        return "You cannot purchase a hotel until you own all the properties of a given color group."
    
    if pa_content == 5:
        return "You cannot purchase a hotel if the property already has one."
    
    if money is not None and money < cost:
        return "You do not have sufficient funds to purchase a hotel at this time."
    
    if pa_content == 4 and nc_content == 5 and pc_content == 4:
        return "Swap North Carolina's hotel with Pennsylvania's 4 houses."
    
    if pa_content == 4 and nc_content == 4 and pc_content == 5:
        return "Swap Pacific's hotel with Pennsylvania's 4 houses."
    
    if houses is not None and (12 - (pc_content + nc_content + pa_content)) > houses:
        return "There are not enough houses available for purchase at this time."
    
    if hotels is not None and hotels < 1:
        return "There are not enough hotels available for purchase at this time."
    
    return purchase_outputs(pc_content, nc_content, pa_content, cost)

def main():
    """
    Main function to execute the Monopoly decision-making process.
    """
    ownership, pc_content, nc_content, pa_content, money, houses, hotels, cost = get_all_info()
    output = all_outputs(ownership, pc_content, nc_content, pa_content, money, houses, hotels, cost)
    print(output)

if __name__ == "__main__":
    main()