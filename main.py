
from src.display import display
from src.read_file import read_file

PATH = "data/orders.csv"


def main():
    
    display(f"\nFirst data file from orders.csv:\n\n{read_file(PATH)}")

    





if __name__ == "__main__":
    main()