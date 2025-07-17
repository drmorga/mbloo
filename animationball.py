#!/usr/bin/env python3
import time
import random
import sys
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_color():
    """Generate a random ANSI color code (bright colors)"""
    return f"\033[1;3{random.randint(1, 6)}m"

def bouncing_ball_animation(name):
    """Display a bouncing ball animation with the user's name"""
    width = 60
    height = 20
    ball = "●"
    pos_x = width // 2
    pos_y = 1
    velocity_y = 1
    gravity = 0.2
    colors = [get_random_color() for _ in range(5)]
    
    try:
        while True:
            clear_screen()
            
            # Update position
            pos_y += velocity_y
            velocity_y += gravity
            
            # Bounce when hitting ground
            if pos_y >= height - 1:
                pos_y = height - 1
                velocity_y = -velocity_y * 0.8
                colors = [get_random_color() for _ in range(5)]  # Change colors on bounce
            
            # Draw the scene
            for y in range(height):
                line = []
                for x in range(width):
                    if y == 0 or y == height - 1:
                        line.append("=")
                    elif x == pos_x and round(y) == round(pos_y):
                        line.append(f"{colors[int(pos_y) % len(colors)]}{ball}\033[0m")
                    else:
                        line.append(" ")
                print("".join(line))
            
            # Display the name
            name_pos = width // 2 - len(name) // 2
            print(" " * name_pos + f"\033[1;35m{name}\033[0m")
            print("\nPress Ctrl+C to quit...")
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nThanks for playing!")
        sys.exit(0)

def main():
    """Main function"""
    clear_screen()
    print("\033[1;36mWelcome to the Bouncing Ball Animation!\033[0m")
    name = input("What's your name? ")
    bouncing_ball_animation(name)

if __name__ == "__main__":
    main()#mbloo
