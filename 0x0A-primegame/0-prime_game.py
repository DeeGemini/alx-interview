#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """
    Returns a list of booleans indicating whether each number up to max_num is prime.
    """
    if max_num < 2:
        raise ValueError("max_num must be at least 2.")

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

def play_game(n, is_prime):
    """
    Returns the winner of the game.
    - 0 for Maria, 1 for Ben
    - None if the game is not over yet
    """
    numbers = list(range(1, n + 1))
    if not numbers:
        raise ValueError("n must be at least 1.")
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        # Find the smallest prime number in the list
        smallest_prime = next((num for num in numbers if is_prime[num]), None)
        
        if smallest_prime is None:  # No primes left to choose
            return turn ^ 1  # The other player wins

        # Remove the prime and its multiples
        numbers = [num for num in numbers if num % smallest_prime != 0]
        turn ^= 1  # Switch turns

def isWinner(x, nums):
    if x is None or nums is None:
        raise ValueError("x and nums must not be None.")
    
    if not nums:
        return None
    
    max_num = max(nums)
    is_prime = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n, is_prime)
        if winner is None:
            raise ValueError("play_game returned None.")
        elif winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
