import customtkinter as ctk


class TaxCalculator:
    def __init__(self) -> None:
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        # Initialize our window
        self.padding: dict = {"padx": 20, "pady": 10}

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax label and entry
        self.tax_label = ctk.CTkLabel(self.window, text="Tax:")
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        # result label and entry
        self.result_label = ctk.CTkLabel(self.window, text="Result:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        # calculate button
        self.calculate_button = ctk.CTkButton(
            self.window, text="Calculate", command=self.calculate
        )
        self.calculate_button.grid(row=3, column=0, columnspan=2, **self.padding)

    def run(self):
        self.window.mainloop()

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate(self):
        try:
            income = float(self.income_entry.get())
            tax = float(self.tax_entry.get())
            result = income * tax / 100
            self.update_result(f"${result:.2f}")
        except ValueError:
            self.update_result("Invalid input")


if __name__ == "__main__":
    tax_calculator = TaxCalculator()
    tax_calculator.run()
