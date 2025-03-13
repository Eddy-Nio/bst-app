import logging
from colorama import Fore, Style
from config import MAX_NUMBERS, MAX_SENTENCE_LENGTH

def get_numbers_input() -> list[int]:
    """
    Get and validate numeric input from user with limits.
    
    Returns:
        list[int]: List of valid integers entered by user
        
    Raises:
        ValueError: If invalid numbers are entered
    """
    while True:
        try:
            numbers = input(f"{Fore.CYAN}\nEnter numbers separated by spaces: {Style.RESET_ALL}").strip()
            if not numbers:
                print(f"{Fore.RED}Error: Empty input{Style.RESET_ALL}")
                continue
                
            nums = [int(num) for num in numbers.split()]
            if len(nums) > MAX_NUMBERS:
                print(f"{Fore.RED}Error: Maximum {MAX_NUMBERS} numbers allowed{Style.RESET_ALL}")
                continue
                
            logging.info(f"Valid number input received: {nums}")
            return nums
            
        except ValueError:
            print(f"{Fore.RED}Error: Please enter valid integers{Style.RESET_ALL}")
            logging.error("Invalid number input received")

def get_sentence_input() -> str:
    """
    Get and validate sentence input with length limit.
    
    Returns:
        str: Valid sentence entered by user
    """
    while True:
        sentence = input(f"{Fore.CYAN}\nEnter a sentence: {Style.RESET_ALL}").strip()
        if not sentence:
            print(f"{Fore.RED}Error: Empty input{Style.RESET_ALL}")
            continue
            
        if len(sentence) > MAX_SENTENCE_LENGTH:
            print(f"{Fore.RED}Error: Maximum {MAX_SENTENCE_LENGTH} characters allowed{Style.RESET_ALL}")
            continue
            
        if not any(c.isalpha() for c in sentence):
            print(f"{Fore.RED}Error: Sentence must contain at least one letter{Style.RESET_ALL}")
            continue
            
        logging.info(f"Valid sentence input received: {sentence}")
        return sentence