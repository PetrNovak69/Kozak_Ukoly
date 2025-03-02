import random
import sys

def interpret(program):
    
    variable = 0


    instructions = program.strip()

   
    i = 0
    while i < len(instructions):
        instruction = instructions[i]

        if instruction == 'I':
          
            try:
                variable = int(input("Zadejte celé číslo: "))
            except ValueError:
                print("Chyba: Neplatný vstup")
                sys.exit(1)
        elif instruction == 'G':
            #
            variable = random.randint(-1024, 1024)
        elif instruction == 'O':

            print(variable)
        elif instruction == '+':
       
            variable += 1
        elif instruction == '-':
      
            variable -= 1
        elif instruction == '0':
       
            variable = 0
        elif instruction == '#':
         
            print("Skript ukončen.")
            break
        else:
            print(f"Chyba: Neznámý příkaz '{instruction}'")
            sys.exit(1)

   
        i += 2 if instruction == 'I' else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Chyba: Není zadán žádný program.")
        sys.exit(1)
    
    program = sys.argv[1]
    interpret(program)
