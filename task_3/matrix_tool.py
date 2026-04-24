import numpy as np

# ================================
# Function to take matrix input
# ================================
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter elements for {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("❌ Error: Number of elements does not match columns")
            return None
        matrix.append(row)

    return np.array(matrix)

# ================================
# Display matrix nicely
# ================================
def display_matrix(title, matrix):
    print(f"\n🔹 {title}")
    print(matrix)

# ================================
# Main Program
# ================================
def main():
    print("====== MATRIX OPERATIONS TOOL ======")

    while True:
        print("\nSelect Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        # ============================
        # ADDITION
        # ============================
        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A is not None and B is not None:
                if A.shape == B.shape:
                    result = A + B
                    display_matrix("Addition Result", result)
                else:
                    print("❌ Matrices must have same dimensions")

        # ============================
        # SUBTRACTION
        # ============================
        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A is not None and B is not None:
                if A.shape == B.shape:
                    result = A - B
                    display_matrix("Subtraction Result", result)
                else:
                    print("❌ Matrices must have same dimensions")

        # ============================
        # MULTIPLICATION
        # ============================
        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A is not None and B is not None:
                if A.shape[1] == B.shape[0]:
                    result = np.dot(A, B)
                    display_matrix("Multiplication Result", result)
                else:
                    print("❌ Columns of A must equal rows of B")

        # ============================
        # TRANSPOSE
        # ============================
        elif choice == "4":
            A = input_matrix("Matrix")

            if A is not None:
                result = A.T
                display_matrix("Transpose Result", result)

        # ============================
        # DETERMINANT
        # ============================
        elif choice == "5":
            A = input_matrix("Matrix")

            if A is not None:
                if A.shape[0] == A.shape[1]:
                    det = np.linalg.det(A)
                    print(f"\n🔹 Determinant: {det}")
                else:
                    print("❌ Determinant only for square matrices")

        # ============================
        # EXIT
        # ============================
        elif choice == "6":
            print("Exiting... ✅")
            break

        else:
            print("❌ Invalid choice")

# Run program
if __name__ == "__main__":
    main()
