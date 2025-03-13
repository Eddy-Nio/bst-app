import logging
from colorama import Fore, Style
from models.trees import BinarySearchTree, WordFrequencyBST
from utils.console import clear_screen, print_menu
from utils.input_handlers import get_numbers_input, get_sentence_input

def main() -> None:
    """
    This function serves as the entry point for the application, providing a menu-driven interface
    for the user to perform various tasks. The available options include sorting numbers in descending
    order and analyzing word frequencies in a given sentence. The function handles user input, executes
    the corresponding tasks, and provides appropriate feedback. It also includes robust error handling
    and logging to ensure smooth operation and easier debugging.
    Menu Options:
    1. Sort numbers - Prompts the user to input a list of numbers, inserts them into a binary search tree,
        and displays the numbers in descending order.
    2. Word frequency - Prompts the user to input a sentence, analyzes the frequency of each word,
        and displays the word counts sorted by frequency.
    q. Quit - Exits the application.
    Error Handling:
    - Catches and logs unexpected errors, providing a message to the user and allowing them to continue.
    - Handles KeyboardInterrupt to allow graceful termination by the user.
    Logging:
    - Logs the start and normal termination of the application.
    - Logs invalid menu selections and unexpected errors with detailed information.
    """
    logging.info("Application started")
    while True:
        try:
            clear_screen()
            print_menu()
            choice = input(f"{Fore.CYAN}\nSelect an option: {Style.RESET_ALL}").lower().strip()
            
            if choice == '1':
                numbers = get_numbers_input()
                bst = BinarySearchTree()
                for num in numbers:
                    bst.insert(num)
                sorted_nums = bst.reverse_in_order()
                print(f"\n{Fore.GREEN}Numbers in descending order:{Style.RESET_ALL}")
                print(" ".join(map(str, sorted_nums)))
                logging.info(f"Numbers sorted: {sorted_nums}")
                
            elif choice == '2':
                sentence = get_sentence_input()
                word_bst = WordFrequencyBST()
                for word in sentence.split():
                    cleaned_word = word.strip(".,!?;:\"'()").lower()
                    if cleaned_word:
                        word_bst.insert(cleaned_word)
                
                word_counts = word_bst.in_order_traversal()
                sorted_counts = sorted(word_counts, key=lambda x: (-x[1], x[0]))
                
                print(f"\n{Fore.GREEN}Word frequencies (sorted by count):{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}----------------------------------{Style.RESET_ALL}")
                for word, count in sorted_counts:
                    print(f"{word:<15}: {count}")
                logging.info(f"Word frequency analysis completed: {dict(sorted_counts)}")
                
            elif choice in ('q', 'quit'):
                print(f"\n{Fore.GREEN}Thank you for using the application!{Style.RESET_ALL}")
                logging.info("Application terminated normally")
                break
                
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose:{Style.RESET_ALL}")
                print("1 - Sort numbers")
                print("2 - Word frequency")
                print("q - Quit")
                logging.warning(f"Invalid menu option selected: {choice}")
            
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Program terminated by user{Style.RESET_ALL}")
            logging.info("Application terminated by user (KeyboardInterrupt)")
            break
        except Exception as e:
            print(f"\n{Fore.RED}An unexpected error occurred: {str(e)}{Style.RESET_ALL}")
            logging.error(f"Unexpected error: {str(e)}", exc_info=True)
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()