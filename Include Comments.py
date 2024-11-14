# Add comments that explain what the code does.
class GitIsAwesomeProgram:

    # Make menu options. 
    def __init__(self):

        self.menu_options = {
            '1': self.print_git_is_awesome,
            '2': self.greet_user,
            '3': self.quit_program,
        }

    def print_git_is_awesome(self):

        print('Git is awesome')
    
    # Get user's name.
    def greet_user(self):
            
            user_input = input("Enter your name: ")

            if user_input.strip():
                
                print(f'Hello, {user_input.strip()}!')

            else:

                print('Hello there!')

    def quit_program(self):

        print('Goodbye!')
        exit()
    
    # Display menu options. 
    def display_menu(self):

        print("\nMenu:")
        print("1. Print 'Git is awesome'")
        print("2. Greet user")
        print("3. Quit")

    def run(self):

        print('Welcome to the Git is Awesome Program!')

        while True:

            self.display_menu()

            # Allow user to pick an option and handle the code defensively.
            choice = input("Enter your choice (1-3): ")
            action = self.menu_options.get(choice)

            if action:
                
                action()


if __name__ == "__main__":
        
        program = GitIsAwesomeProgram()
        program.run()