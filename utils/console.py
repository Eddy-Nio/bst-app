import os
from colorama import Fore, Style

def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Display the application menu."""
    print(f"\n{Fore.GREEN}=== BST Applications ==={Style.RESET_ALL}")
    print("1. Sort numbers in descending order")
    print("2. Count word frequencies")
    print("q. Quit program")
    print(f"{Fore.GREEN}====================={Style.RESET_ALL}")